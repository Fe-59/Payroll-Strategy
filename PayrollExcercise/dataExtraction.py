"""
This script contains the classes to extract Data from the Text file
"""

############################# Import Required libraries #################################

from __future__ import annotations
from abc import ABC, abstractclassmethod
from typing import List

################################## Define ETL Classes ###################################

class DataExtractor:

    # ------------- Define a Class Attribute to get the Text File -------------- #
    file = input("\033[1;32;40m \n ------------------- Wellcome to the Payroll System -------------------\n\n Please Enter Text File Path:") 

    def __init__(self, information: RecordType) -> None:
        """ Set the strategy to be used, at the instantiation.
        """        
        self._information = information       

    @classmethod
    def readFile(cls) -> List:
        """
        Takes the class attribute and returns a list with the information of every single person.
        """        
        with open(cls.file, encoding='utf-8') as f:
            lines = f.readlines()
            lines = [i.strip('\n') for i in lines if i != '\n'] # ---------------- Remove empty rows ---------------- #
            lines = list(dict.fromkeys(lines))                  # ------------ Get rid of Repeated rows ------------- #

        return lines

    def InformationPicker(self) -> List:
        """ Get information based on the implemented strategy
        """
        return self._information.get_record(self.readFile())
         


class RecordType(ABC):
    """ Define a strategy template to extract data from text file, either employees or their corresponding days worked.
    """    
    @abstractclassmethod
    def get_record(self, data:List):
        pass

class Employees(RecordType):

    def get_record(self, data:List) -> List:
        record = [i.split('=') for i in data]
        employees = [j[0] for j in record]
        return employees

class WorkedHours(RecordType):

    def get_record(self, data:List) -> List:
        record = [i.split('=') for i in data]
        hours = [j[1] for j in record]
        return hours    
       