import pypdf

#Interface-Implementierung
from PythonFileManagementInterfaces.STDFileInterface import STDFileInterface
import os

"""
    Klasse die das STDFileInterface implementiert um 
    eine höhere Kompatibilität und Unabhängigkeit zu gewährleisten.
"""


class PDFImplementation(STDFileInterface):
    def __init__(self):
        self.totalFile = None
        self.filename = None
        self.path = None

    #default-Konnstruktor
    def initialize(self, path: str, filename: str):
        self.setFile(path,  filename)

    #Prints the private data of the class
    def printData(self):
        print(self)
        print(self.path)
        print(self.filename)
        print(self.totalFile)

    #Smart setter, which checks the primary Features of the given path.
    def setFile(self, filepath: str, filename: str):
        if not filepath.endswith("\\") and not filename.startswith("\\"):
            filepath += "\\"
            self.path = filepath
            self.filename = filename
            self.totalFile = filepath + filename
            return
        else:
            self.path = filepath
            self.filename = filename
            self.totalFile = filepath + filename
            return

    #append on file onto another
    def appendFile(self, filepath: str, fileName: str):
        pdfWriter = pypdf.PdfWriter()
        pdfReader = pypdf.PdfReader(self.totalFile)

        for page in range(len(pdfReader.pages)):
            pdfWriter.add_page(pdfReader.pages[page])

        if not filepath.endswith("\\") and not fileName.startswith("\\"):
            filepath += "\\"

        additionalPdfPath = os.path.join(filepath, fileName)
        additionalPdfReader = pypdf.PdfReader(additionalPdfPath)

        for page in range(len(additionalPdfReader.pages)):
            pdfWriter.add_page(additionalPdfReader.pages[page])

        with open(self.totalFile, "wb") as output_file:
            pdfWriter.write(output_file)

    def deleteFile(filepath: str, fileName: str):
        pass
