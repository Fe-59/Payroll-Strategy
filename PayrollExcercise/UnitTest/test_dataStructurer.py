import unittest
from dataStructurer import *
from unittest import TestCase
from unittest.mock import patch


class  Tester(TestCase):  

    hours = ['MO10:00-12:00,TU10:00-12:00, WE19:00-00:00,TH16:00-20:00, SA14:00-18:00,SU20:00-21:00, MO01:00-05:00, TU00:01-03:00,WE01:00-03:00,TH14:00-18:00,FR20:00-00:00']
    expectedResult = [{0: ['10:00-12:00', '01:00-05:00'],
                        1: ['10:00-12:00', '00:01-03:00'],
                        2: ['19:00-00:00', '01:00-03:00'],
                        3: ['16:00-20:00', '14:00-18:00'],
                        4: ['20:00-00:00'],
                        5: ['14:00-18:00'],
                        6: ['20:00-21:00']}]      
    @classmethod    
    def test_DataWrapper(cls):
        result = DataWrapper(cls.hours).dataParser()
        Tester().assertEqual(result, cls.expectedResult)

    @classmethod 
    def test_DataWrapper(cls):
        with patch('dataStructurer.DataWrapper.dataParser') as mocked_get:
            mocked_get.return_value = cls.expectedResult

            result = DataWrapper(cls.hours).dataParser()
            Tester().assertEqual(result, cls.expectedResult)


if __name__ == '__main__':
    unittest.main()