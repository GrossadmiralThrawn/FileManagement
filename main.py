# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import PythonFileManagementInterfaces.STDFileInterface
from PythonFileManagementInterfaces.STDFileInterface import STDFileInterface
from implementations.PDFImplementation import PDFImplementation

alreadyinitialized = False


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}.')  # Press Strg+F8 to toggle the breakpoint.


def wellBeing():
    response = input("Wie geht es dir?\n")
    if ((response.__contains__("Gut") or response.__contains__("gut") or response.__contains__("besser")) and not (
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


def initialize(type: str):
    if type.__contains__("PDFImplementation"):
        basepath = input("Wo liegt die Datei mit der das verarbeitende Objekt initialisiert werden soll?\n")
        basefile: str = input("Wie heißt die Datei, welche zur Objektinitialisierung verwendet werden solL?\n")
        return PDFImplementation(basepath, basefile)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sTDFileInterface = STDFileInterface()

    print_hi('Lukas')
    wellBeing()



    selectFileType = input("Möchtest du mit PDFs arbeiten? \nYes or no: y/ n\n")

    if selectFileType == "y":
        sTDFileInterface = initialize("PDFImplementation")
    else:
        print("Leider steht aktuell noch keine weitere Implementierung zur Verfügung. Deswegen kann ich dir leider gerade nicht helfen. Ich schalte mich jetzt ab, aktiviere mich"
              "aber gerne wieder, wenn ich dir helfen kann. Ich wünsche dir noch eine schöne und gute Zeit und bis zum nächsten Mal. :)\n")

    while (True):
        print("Du hast folgende Möglichkeiten:")
        print()
        print("1: Zwei PDFs mergen")
        print("2: Mehrere PDFs mergen")
        print("3: Mehrere PDFs mergen, aber ohne die Objektinitialisierungsdatei.")
        print("0: Programm beenden.")

        userInput = input()
        if (userInput == "1"):
            filepath = input("Dateipfad: ")
            filename = input("Dateiname: ")
            outputname = input("Wie soll die ausgegebene Datei heißen? ")
            sTDFileInterface.mergeFile(filepath, filename, "C:\\Users\\Lukas\\Pictures\\Screenshots", outputname)
        if (userInput == "2"):
            pass
        if (userInput == "3"):
            pass
        if (userInput == "0"):
            break

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
