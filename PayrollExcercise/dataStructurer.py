from __future__ import annotations
from typing import List, Dict



class DataWrapper:
  
    """ This task involves a data structuring problem since the input data requires to be organized previous to find the salaray
        of each employee
    """

    def __init__(self, workedHours:List) -> None:
      self._workedHours = workedHours

    def tupler(self, chronicle:List) -> List:
      """ This method takes a list of unstructured data and applies the following criteria to converet it into tuples of (day, worked hours):
          MO: Monday, TU: Tuesday, WE: Wednesday, TH: Thursday, FR: Friday, SA: Saturday, SU: Sunday
      """
      count = 0
      for i in chronicle:
        i = (i.strip(' ')[:2], i.strip(' ')[2:])
        chronicle[count] = i
        count += 1
      return chronicle

    def dataCollector(self, recordList: List) -> Dict:
      """ This method returns a dictionary of days and their correposding worked hours.
          recordList parameter must be a list of tuples which cointais the days and the corresponding worked hours.
      """
      MO = [i[1] for i in recordList if i[0]=='MO']
      TU = [i[1] for i in recordList if i[0]=='TU']
      WE = [i[1] for i in recordList if i[0]=='WE']
      TH = [i[1] for i in recordList if i[0]=='TH']
      FR = [i[1] for i in recordList if i[0]=='FR']
      SA = [i[1] for i in recordList if i[0]=='SA']
      SU = [i[1] for i in recordList if i[0]=='SU']
      
      """ For better approach, we replace the used nomenclature of days with numbers:
          MO: 0, TU: 1, WE: 2, TH: 3, FR: 4, SA: 5, SU: 6
      """
      days = ['MO', 'TU', 'WE', 'TH', 'FR', 'SA', 'SU']

      payDays = {}
      for idx,day in enumerate(days):
        if len(locals()[day]) > 0:
          payDays[idx] = locals()[day]
                
      return payDays
    
    def dataParser(self) -> List:
      """ This method takes the raw data and converts it in a list of dictionaries
      """
      globalRecord = [i.split(',') for i in self._workedHours]

      count = 0
      for i in globalRecord:
        globalRecord[count] = self.tupler(i)
        count += 1

      structuredRecords = []
      for i in globalRecord:
        structuredRecords.append(self.dataCollector(i))
                   
      return structuredRecords

    # This is an example of the structured data after being processed by this class
    """
      [{0: ['10:00-12:00', '01:00-05:00'],
        1: ['10:00-12:00', '00:01-03:00'],
        2: ['19:00-00:00', '01:00-03:00'],
        3: ['16:00-20:00', '14:00-18:00'],
        4: ['20:00-00:00'],
        5: ['14:00-18:00'],
        6: ['20:00-21:00']},

       {1: ['10:00-12:00', '15:00-19:00'],
        4: ['12:00-14:00', '20:00-02:00'],
        5: ['20:00-21:00']},
        
       {0: ['08:00-08:00', '10:00-16:00'],
        3: ['10:00-14:00', '16:00-22:00'],
        6: ['20:00-23:00']}]
    """
