from dataclasses import dataclass
import re

from dataclasses_json import dataclass_json

INVOICES_PATTERNS = {
    r'Energia Elétrica': 5,
    r'Energia SCEE s/ ICMS': 5,
    r'Energia compensada GD I': 5,
    r'Contrib Ilum Publica Municipal': 1,
    r'Multa \d+% sobre conta de': 1,
    r'Juros \d+%am sobre conta \d/\d': 1,
    r'Correção IPCA/IGPM s/ conta \d/\d': 1
}

@dataclass_json
@dataclass
class ElectricityInvoice:
    name: str
    unity: str
    amount: float
    unit_price: float
    value: float


@dataclass_json
@dataclass
class ContributionTaxInvoice:
    name: str
    value: float


class InvoiceFactory:
    @staticmethod
    def create_invoice(content, size):
        if size == 5:
            return ElectricityInvoice(name=content[0], unity=content[1], amount=content[2], unit_price=content[3],
                                      value=content[4])
        elif size == 1:
            return ContributionTaxInvoice(name=content[0], value=content[1])


class ParseDataException(Exception):
    pass


class InvoicedAmountsParser:

    @staticmethod
    def parse_data(data, start_marker, end_marker):
        try:
            initial_index = data.index(start_marker)
            final_index = data.index(end_marker)
            total_index = data.index("TOTAL")
        except ValueError:
            raise ParseDataException("Failed to parse data between markers")
        return {"invoices": InvoicedAmountsParser.__extract_data(data[initial_index:final_index]),
                "total": data[total_index + 1]}

    @staticmethod
    def __extract_data(data):
        invoices = []
        for pattern, size in INVOICES_PATTERNS.items():
            regex = re.compile(pattern)
            for index, text in enumerate(data):
                if regex.match(text):
                    content = data[index:index + size + 1]
                    invoice = InvoiceFactory.create_invoice(content, size)
                    invoices.append(invoice)
                    data = data[index + size + 1:]
                    break
        return invoices

    @staticmethod
    def parse(data):
        start_marker = "Energia Elétrica"
        end_marker = "Histórico de Consumo"

        extracted_data = InvoicedAmountsParser.parse_data(data, start_marker, end_marker)

        return {"name": "invoices", "content": extracted_data}
