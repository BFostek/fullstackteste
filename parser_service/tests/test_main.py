import json
from unittest import TestCase

from main import process_file, convert_to_json


class Test(TestCase):
    def test_parse_object(self):
        result = process_file('/home/brenomartins/Documents/FATURAS/faturas/3001165684-11-2023.pdf')
        try:
            data =  convert_to_json(result)
            print(data)
        except Exception as e:
            self.fail("Was not able to parse file to json")
