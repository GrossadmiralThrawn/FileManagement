import pypdf

from PythonFileManagementInterfaces.STDFileInterface import STDFileInterface


class PDFImplementation(STDFileInterface):
    def __init__(self):
        self.totalFile = None
        self.filename = None
        self.path = None

    def initialize(self, path: str, filename: str):
        self.path = path
        self.filename = filename
        self.totalFile = path + filename

    def printData(self):
        print(self.path)
        print(self.filename)

    def setFile(self, filepath: str, fileName: str):
        pass

    def appendFile(self, filepath: str, fileName: str):
        pdfWriter = pypdf.PdfWriter()
        pdfReader = pypdf.PdfReader(self.totalFile)

        for page in range(len(pdfReader.pages)):
            pdfWriter.add_page(pdfReader.pages[page])

        # Read the existing PDF and append its pages

        with open(self.path, "wb") as output_file:
            pdfWriter.write(output_file)

    def deleteFile(filepath: str, fileName: str):
        pass
