# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import implementations.PDFImplementation
import PythonFileManagementInterfaces


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.


def printTestData(sTDFileInterface):
    sTDFileInterface.printData()
    pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    pDFImplementation = implementations.PDFImplementation.PDFImplementation()
    pfad = input("Dateipfad: ")
    filename = input("Dateiname: ")


    pDFImplementation.initialize(pfad, filename)
    printTestData(pDFImplementation)

    pfad = input("Pfad zur anzuhängende Datei: ")
    filename = input("Dateiname: ")


    pDFImplementation.appendFile(pfad, filename)
    print("Hallo Welt")

# C:\Frank_Schätzing_Der_Schwarm\
# Personalbogen_blanko.pdf
# verbindliche_Anmeldung_Teamertreffen_2024.pdf
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
