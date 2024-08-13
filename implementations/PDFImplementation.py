import pypdf
from PythonFileManagementInterfaces.STDFileInterface import STDFileInterface
import os


class PDFImplementation(STDFileInterface):
    def __init__(self, path: str, filename: str):
        self.setFile(path, filename)


    def initialize(self, path: str, filename: str):
        self.setFile(path, filename)

    def printData(self):
        print(f"Path: {self.path}, Filename: {self.filename}, Total File: {self.totalFile}")

    def setFile(self, filepath: str, filename: str):
        if not filename.endswith(".pdf"):
            filename += ".pdf"

        self.path = filepath
        self.filename = filename
        self.totalFile = os.path.join(filepath, filename)

    def getFile(self):
        return self.totalFile

    def appendFile(self, filepath: str, fileName: str):
        pdfWriter = pypdf.PdfWriter()
        pdfReader = pypdf.PdfReader(self.totalFile)

        for page in range(len(pdfReader.pages)):
            pdfWriter.add_page(pdfReader.pages[page])

        additionalPdfPath = os.path.join(filepath, fileName)
        additionalPdfReader = pypdf.PdfReader(additionalPdfPath)

        for page in range(len(additionalPdfReader.pages)):
            pdfWriter.add_page(additionalPdfReader.pages[page])

        with open(self.totalFile, "wb") as output_file:
            pdfWriter.write(output_file)

    def mergeFile(self, filepath: str, fileName: str = None, outputPath: str = None, outputName: str = None):
        pdfWriter = pypdf.PdfWriter()

        # Prüfe, ob die Initialdatei existiert
        if not os.path.exists(self.totalFile):
            print(f"Fehler: Die Datei {self.totalFile} existiert nicht.")
            return

        pdfReader = pypdf.PdfReader(self.totalFile)

        for page in range(len(pdfReader.pages)):
            pdfWriter.add_page(pdfReader.pages[page])

        # Wenn kein Dateiname angegeben ist, benutze den Dateinamen der Initialdatei
        if fileName is None:
            fileName = os.path.basename(self.totalFile)

        # Wenn kein Verzeichnispfad angegeben ist, benutze das Verzeichnis der Initialdatei
        if filepath is None:
            filepath = self.path

        additionalPdfPath = os.path.join(filepath, fileName)

        # Prüfe, ob die zusätzliche Datei existiert
        if not os.path.exists(additionalPdfPath):
            print(f"Fehler: Die Datei {additionalPdfPath} existiert nicht.")
            return

        additionalPdfReader = pypdf.PdfReader(additionalPdfPath)

        for page in range(len(additionalPdfReader.pages)):
            pdfWriter.add_page(additionalPdfReader.pages[page])

        # Wenn kein Ausgabepfad angegeben ist, benutze das Verzeichnis der Initialdatei
        if outputPath is None:
            outputPath = self.path

        # Wenn kein Ausgabename angegeben ist, benutze den Namen "merged_output.pdf"
        if outputName is None:
            outputName = "merged_output.pdf"

        outputFilePath = os.path.join(outputPath, outputName)

        with open(outputFilePath, "wb") as output_file:
            pdfWriter.write(output_file)
    def mergeFiles(self, filepaths, outputPath: str, outputName: str):
        # Füge self.totalFil zu filepaths hinzu
        if self.totalFile is not None:
            filepaths.append(self.totalFile)

        pdfWriter = pypdf.PdfWriter()

        for filepath in filepaths:
            pdfReader = pypdf.PdfReader(filepath)
            for page in range(len(pdfReader.pages)):
                pdfWriter.add_page(pdfReader.pages[page])

        outputFilePath = os.path.join(outputPath, outputName)

        with open(outputFilePath, "wb") as output_file:
            pdfWriter.write(output_file)

    def searchFile(self, filepath: str, fileName: str):
        if not fileName.endswith(".pdf"):
            fileName += ".pdf"
        return os.path.exists(os.path.join(filepath, fileName))

    def mergeFilesWithoutInternalFile(self, filepaths, outputPath: str, outputName: str):
        pdfWriter = pypdf.PdfWriter()

        for filepath in filepaths:
            pdfReader = pypdf.PdfReader(filepath)
            for page in range(len(pdfReader.pages)):
                pdfWriter.add_page(pdfReader.pages[page])

        outputFilePath = os.path.join(outputPath, outputName)

        with open(outputFilePath, "wb") as output_file:
            pdfWriter.write(output_file)

    def deleteFile(self, filepath: str, fileName: str):
        if not fileName.endswith(".pdf"):
            fileName += ".pdf"
        file_to_delete = os.path.join(filepath, fileName)
        if os.path.exists(file_to_delete):
            os.remove(file_to_delete)
            return True
        return False

    def deleteExternalFile(self, filepath: str, fileName: str):
        return self.deleteFile(filepath, fileName)

    def splitFile(self, position: int):
        pdfReader = pypdf.PdfReader(self.totalFile)
        pdfWriter1 = pypdf.PdfWriter()
        pdfWriter2 = pypdf.PdfWriter()

        for page in range(position):
            pdfWriter1.add_page(pdfReader.pages[page])

        for page in range(position, len(pdfReader.pages)):
            pdfWriter2.add_page(pdfReader.pages[page])

        base, ext = os.path.splitext(self.totalFile)
        part1 = f"{base}_part1{ext}"
        part2 = f"{base}_part2{ext}"

        with open(part1, "wb") as output_file1:
            pdfWriter1.write(output_file1)
        with open(part2, "wb") as output_file2:
            pdfWriter2.write(output_file2)

    def splitExternFile(self, filepath: str, fileName: str, position: int, nameNewFile: str):
        if not fileName.endswith(".pdf"):
            fileName += ".pdf"
        file_to_split = os.path.join(filepath, fileName)

        pdfReader = pypdf.PdfReader(file_to_split)
        pdfWriter = pypdf.PdfWriter()

        for page in range(position, len(pdfReader.pages)):
            pdfWriter.add_page(pdfReader.pages[page])

        new_file_path = os.path.join(filepath, nameNewFile)

        with open(new_file_path, "wb") as output_file:
            pdfWriter.write(output_file)

    def appendFileNameIncluded(self, filepath: str):
        fileName = os.path.basename(filepath)
        dirPath = os.path.dirname(filepath)
        self.appendFile(dirPath, fileName)
