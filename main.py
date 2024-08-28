import PythonFileManagementInterfaces.STDFileInterface
from implementations.PDFImplementation import PDFImplementation


def print_hi(name):
    print(f'Hi, {name}.')


def wellBeing():
    response = input("Wie geht es dir?\n")
    if ("gut" in response.lower() or "besser" in response.lower()) and "nicht" not in response.lower():
        print("Schön zu hören. :)")
    else:
        print("Das tut mir leid. Ich hoffe es geht dir bald wieder besser. ")

    if "und dir" in response.lower() or "und selbst" in response.lower():
        print("Mir geht es gut, danke. :)")


def appendInteraction(stdFileInterface: PythonFileManagementInterfaces.STDFileInterface):
    pfad = input("Pfad zur anzuhängenden Datei: ")
    filename = input("Dateiname: ")
    stdFileInterface.appendFile(pfad, filename)


def initialize(type: str):
    if type == "PDFImplementation":
        basepath = input("Wo liegt die Datei mit der das verarbeitende Objekt initialisiert werden soll?\n")
        basefile = input("Wie heißt die Datei, welche zur Objektinitialisierung verwendet werden soll?\n")
        return PDFImplementation(basepath, basefile)


if __name__ == '__main__':
    print_hi('Lukas')
    wellBeing()

    sTDFileInterface = None

    selectFileType = input("Möchtest du mit PDFs arbeiten? \nYes or no: y/ n\n")

    if selectFileType.lower() == "y":
        sTDFileInterface = initialize("PDFImplementation")
    else:
        print("Leider steht aktuell noch keine weitere Implementierung zur Verfügung. "
              "Ich wünsche dir noch eine schöne und gute Zeit und bis zum nächsten Mal. :)")
        exit()

    while True:
        print("\nDu hast folgende Möglichkeiten:")
        print("1: Zwei PDFs mergen")
        print("2: Mehrere PDFs mergen")
        print("3: Mehrere PDFs mergen, aber ohne die Objektinitialisierungsdatei.")
        print("0: Programm beenden.")

        userInput = input("Bitte wähle eine Option: ")

        if userInput == "1":
            filepath = input("Dateipfad: ")
            filename = input("Dateiname: ")
            newFilePosition = input("Wo soll die neue Datei liegen? ")
            outputname = input("Wie soll die ausgegebene Datei heißen? ")
            sTDFileInterface.mergeFile(filepath, filename, newFilePosition, outputname)

        elif userInput == "2":
            print("Option zum Merger mehrerer PDFs noch nicht implementiert.")
            pass  # Future implementation for merging multiple PDFs

        elif userInput == "3":
            print("Option zum Merger mehrerer PDFs ohne Initialisierungsdatei noch nicht implementiert.")
            pass  # Future implementation for merging multiple PDFs without the initialization file

        elif userInput == "0":
            print("Bis zum nächsten Mal. :)")
            break

        else:
            print("Ungültige Auswahl, bitte versuche es erneut.")
# C:\Users\Lukas\Pictures\Screenshots
# Personalbogen_blanko.pdf
# verbindliche_Anmeldung_Teamertreffen_2024.pdf
# C:\Users\Lukas\Desktop\SP2024-G4-Kinobetreiber
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


#Variante Laptop
#C:\Users\lukas\Desktop\TestOrdner
#\Test.pdf
#\Test2.pdf
#C:\Users\Lukas\Downloads
