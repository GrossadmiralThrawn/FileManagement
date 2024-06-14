# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import implementations.PDFImplementation
import PythonFileManagementInterfaces.STDFileInterface


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}.')  # Press Strg+F8 to toggle the breakpoint.


def wellBeing():
    response = input("Wie geht es dir?\n")
    if ((response.__contains__("Gut") or response.__contains__("gut")) and not (
            response.__contains__("Nicht") or response.__contains__("nicht"))):
        print("Schön zu hören. :)")
    else:
        print("Das tut mir leid. Ich hoffe es geht dir bald wieder besser. ")

    if response.__contains__("und dir") or response.__contains__("Und dir") or response.__contains__(
            "und selbst") or response.__contains__("Und selbst"):
        print("Mir geht es gut, danke. :)")


def printTestData(sTDFileInterface):
    sTDFileInterface.printData()


def appendInteraction(stdFileInterface: PythonFileManagementInterfaces.STDFileInterface):
    pfad = input("Pfad zur anzuhängende Datei: ")
    filename = input("Dateiname: ")

    stdFileInterface.appendFile(pfad, filename)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pDFImplementation = implementations.PDFImplementation.PDFImplementation()


    print_hi('Lukas')
    wellBeing()


    pfad = input("Dateipfad: ")
    filename = input("Dateiname: ")
    pDFImplementation.initialize(pfad, filename)


    pfad = input("Dateipfad: ")
    filename = input("Dateiname: ")
    targetPath = input("Target Path: ")
    targetName = input("Target Name: ")

    pDFImplementation.mergeFile(pfad, filename, targetPath, targetName)

    print("Bis zum nächsten Mal. :)")

# C:\Users\Lukas\Pictures\Screenshots
# Personalbogen_blanko.pdf
# verbindliche_Anmeldung_Teamertreffen_2024.pdf
# C:\Users\Lukas\Desktop\SP2024-G4-Kinobetreiber
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


#Variante Laptop
#C:\Users\lukas\Desktop\TestOrdner
#\Test.pdf
#\Test2.pdf
