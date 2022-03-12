from dataExtraction import *
from dataStructurer import *
from moneyMaker import *


if __name__ == '__main__':
    employees = DataExtractor(Employees()).InformationPicker()
    workedHours = DataExtractor(WorkedHours()).InformationPicker()
    structuredHours = DataWrapper(workedHours).dataParser()

    print('\n')
    for i in range(len(structuredHours)):        
        print(str(i+1)+'.-', f'The amount to pay {employees[i]} is {Accountant().fairFather(structuredHours[i])}')
    print('\n')

