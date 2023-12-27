import logging

from parsers.sections.consumption_history_parser import ConsumptionHistoryParser
from parsers.sections.invoiced_amounts_parser import InvoicedAmountsParser
from parsers.sections.nfe_info_parser import NfeInfoParser


class ElectricityBillParser:
    def __init__(self, data_array):
        self._data = data_array[0]
        self._sections = [NfeInfoParser, ConsumptionHistoryParser, InvoicedAmountsParser]

    def parse(self):
        try:
            result = {}
            for section in self._sections:
                item = section.parse(self._data)
                result[item['name']] = item['content']
            return result
        except Exception as e:
            logging.error(e)
            return False

