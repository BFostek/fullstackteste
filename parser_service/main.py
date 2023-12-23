from parsers.ElectricityBillParser import ElectricityBillParser
from pdfFormatter import pdf_to_array


def main():
    print(ElectricityBillParser(pdf_to_array("faturas/3001165684-10-2023.pdf")).parse())
    print("Hello World")


if __name__ == "__main__":
    main()
