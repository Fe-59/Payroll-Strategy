from __future__ import annotations
from abc import ABC, abstractclassmethod
from typing import List, Dict, Set, Sequence, Optional, Type
import datetime as dt


class Accountant:
    #-------- Once our data is structured, we proceed to calculate the salary per each employee --------#
    #-------------- Therefore, we need to apply the following criteria for every employee --------------#
    """
        Monday - Friday
        00:01 - 09:00 25 USD -----> Early
        09:01 - 18:00 15 USD -----> Normal
        18:01 - 00:00 20 USD -----> After

        Saturday & Sunday
        00:01 - 09:00 30 USD -----> Early
        09:01 - 18:00 20 USD -----> Normal
        18:01 - 00:00 25 USD -----> After
    """

    """ One of the most interesting concerns is the hours worked during different salary ranges,
        The following methods consider all those scenarios to avoid collisions.
    """

    def __init__(self) -> None:
      self._weekdayRate = SalaryWeekday()
      self._weekendRate = SalaryWeekend()    

    def timeReader(self, hour: str) -> dt.datetime:
      """ This method takes as input a string time and converts it into a 24H format integer
      """
      return dt.datetime.strptime(hour, '%H:%M').time().hour

    #------------------------------------- Key Method ------------------------------------#
    def validRecord(self, individualRecord: Dict) -> Dict:
      """ This method converts a dictionary of string intervals into a dictionary of ranges,
          the key step of this method is to assing each range to the corresponding day when 
          you have transition intervals between journeys, specially for Friday-Saturday 
          and Sunday-Monday becasue we apply different salary criterias for those periods.
      """        
      cleanedRecord = []

      for idx,lineRecord in enumerate(individualRecord.items()):
        parsedStringTime = []
        nextDayRanges = []  

        for stringTime in lineRecord[1]:
          steps = [self.timeReader(i) for i in stringTime.split('-')]

          if steps[1] == 0:
            steps[1] = 24
            parsedStringTime.append(range(steps[0],steps[1]))

          elif steps[1] < steps[0]:
            steps.insert(2,steps[1])

            parsedStringTime.append(range(steps[0],24))
            nextDayRanges.append(range(0,steps[2]))
            # print("\033[1;32;40m", nextDayRanges)

          else:
            parsedStringTime.append(range(steps[0],steps[1]))

        cleanedRecord.append((lineRecord[0],parsedStringTime))
        if nextDayRanges:
          cleanedRecord.append(((lineRecord[0]+1),nextDayRanges))

      """ cleanedRecord is a list of tuples wich contains the days and their corresponding worked hours,
          next step is to convert it into a dictionary of lists, considering the new created worked ranges 
          because of transitions between midnight such as the one shown below:

                                                                            [
          {1: ['10:00-12:00','15:00-19:00','22:00-03:00',                   (1, [range(10, 12), range(15, 19), range(22, 24), range(19, 24), range(23, 24)]),
               '19:00-01:00','23:00-04:00'],                                (2, [range(0, 3), range(0, 1), range(0, 4)]),
           2: ['08:00-10:00','20:00-03:00'],                  ---------->   (2, [range(8, 10), range(20, 24)]),
           4: ['12:00-14:00', '20:00-02:00', '23:00-01:00'],                (3, [range(0, 3)]),
           5: ['20:00-21:00']}                                              (4, [range(12, 14), range(20, 24), range(23, 24)]),
                                                                            (5, [range(0, 2), range(0, 1)]),
                                                                            (5, [range(20, 21)])
                                                                            ]            
      """
      hmtimes = []
      parsedRecord = {}
      for i in range(len(cleanedRecord)):
        hmtimes.append(int(cleanedRecord[i][0]))
        counter = {_:hmtimes.count(_) for _ in hmtimes} #---------------- Count days within cleanRecord list -------------#

      if len(counter)==len(cleanedRecord):              #----------------- If counter and cleanRecord have the same number of elements -------------#
        parsedRecord = dict(cleanedRecord)

      else:
        repeated = [m for m in counter.keys() if counter[m]>1] #-------------------- Create a list of repeated days -----------------#        
        indexes = {}
        for r in repeated:                                     #------------- Find indexes of repeated days in cleanRecord -----------#
          indexes[r] = [cleanedRecord.index(n) for n in cleanedRecord if int(n[0]) == r]
        
        dawnings = []
        for key in indexes.keys():
          keys = indexes[key]
          day_rec = [cleanedRecord[i][1] for i in keys]

          for rec in day_rec[1:]:
            day_rec[0].extend(k for k in rec)
          day_rec = day_rec[0]         
          dawnings.append(day_rec)
        
        parsedRecord = dict(cleanedRecord)
        for r in range(len(repeated)):
          parsedRecord[repeated[r]] = dawnings[r]

      """ Finally, we get the dictionary with the right corresponding work ranges:

      [
      (1, [range(10, 12), range(15, 19), range(22, 24), range(19, 24), range(23, 24)]),     {
      (2, [range(0, 3), range(0, 1), range(0, 4)]),                                         1: [range(10, 12),range(15, 19),range(22, 24),range(19, 24),range(23, 24)],
      (2, [range(8, 10), range(20, 24)]),                                           ----->  2: [range(0, 3), range(0, 1), range(0, 4), range(8, 10), range(20, 24)],
      (3, [range(0, 3)]),                                                                   3: [range(0, 3)],
      (4, [range(12, 14), range(20, 24), range(23, 24)]),                                   4: [range(12, 14), range(20, 24), range(23, 24)],
      (5, [range(0, 2), range(0, 1)]),                                                      5: [range(0, 2), range(0, 1), range(20, 21)] 
      (5, [range(20, 21)])                                                                  }
      ]           
      """          
      
      return parsedRecord


    def Calculator(self, payStrategy: SalaryRate, workRanges: Sequence) -> int:
      """We use this method to instantiate the Strategy to be applied"""
      return payStrategy.cashier(workRanges)


    def fairFather(self, fullWork: Dict) -> int:
      """ This is the method which computes the total amount to be payed
          per each employee
      """

      workRanges = self.validRecord(fullWork)

      total = []
      for i in workRanges.keys():

        if i in range(0,5):
          payMethod = self._weekdayRate        
        else:
          payMethod = self._weekdayRate
        
        cash = self.Calculator(payMethod,workRanges[i]) #------ Compute pay of Each Day ------#
        total.append(sum(cash))      
      return sum(total)



#------------------------- Strategy Templates ----------------------------------#

class SalaryRate(ABC):
    """ Strategy template to determine the amount to pay according to the 
        Salary range
    """
    early = range(0, 9)
    normal = range(9, 18)
    after = range(18, 24)              

    @abstractclassmethod
    def cashier(cls, intervals:Sequence):
      pass


class SalaryWeekday(SalaryRate):
    """ This method takes as input a list of work ranges and returns a list
        with the salary for each one of them using the weekday criteria
    """  

    @classmethod
    def cashier(cls, intervals:Sequence) -> List:    
      cash = []
      payTotal = []
      for period in intervals:

        for hour in period:
          if hour in cls.early:
            cash.append(25)
          elif hour in cls.normal:
            cash.append(15)
          elif hour in cls.after:
            cash.append(20)          
          pay_of_range = sum(cash)
        payTotal.append(pay_of_range)
      return payTotal


class SalaryWeekend(SalaryRate):
    """ This method takes as input a list of work ranges and returns a list
        with the salary for each one of them using the weekend criteria
    """  

    @classmethod
    def cashier(cls, intervals:Sequence) -> List:    
      cash = []
      payTotal = []
      for period in intervals:

        for hour in period:
          if hour in cls.early:
            cash.append(30)
          elif hour in cls.normal:
            cash.append(20)
          elif hour in cls.after:
            cash.append(25)          
          pay_of_range = sum(cash)
        payTotal.append(pay_of_range)
      return payTotal
