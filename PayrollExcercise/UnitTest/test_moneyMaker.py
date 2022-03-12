import unittest
from moneyMaker import *
from unittest import TestCase
from unittest.mock import patch


class  moneyTester(TestCase):  

    structuredhours =   [{0: ['10:00-12:00', '01:00-05:00'],
                          1: ['10:00-12:00', '00:01-03:00'],
                          2: ['19:00-00:00', '01:00-03:00'],
                          3: ['16:00-20:00', '14:00-18:00'],
                          4: ['20:00-00:00'],
                          5: ['14:00-18:00'],
                          6: ['20:00-21:00']}]

    expectedResult = 905

    @classmethod    
    def test_Accountant(cls):
        result = Accountant().fairFather(cls.structuredhours)
        moneyTester().assertEqual(result, cls.expectedResult)

    @classmethod 
    def test_Accountant(cls):
        with patch('moneyMaker.Accountant.fairFather') as mocked_get:
            mocked_get.return_value = cls.expectedResult

            result = Accountant().fairFather(cls.structuredhours)
            moneyTester().assertEqual(result, cls.expectedResult)


if __name__ == '__main__':
    unittest.main()