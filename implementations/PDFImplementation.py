import os
import pypdf
from PythonFileManagementInterfaces.STDFileInterface import STDFileInterface


class PDFImplementation(STDFileInterface):
    def __init__(self, path: str, filename: str):
        self.setFile(path, filename)

    def initialize(self, path: str, filename: str):
        self.setFile(path, filename)

    def printData(self):
        print(f"Path: {self.path}, Filename: {self.filename}, Total File: {self.totalFile}")

    def setFile(self, filepath: str, filename: str):
        filename = self.ensure_pdf_extension(filename)
        self.path = filepath
        self.filename = filename
        self.totalFile = os.path.join(filepath, filename)

    def getFile(self):
        return self.totalFile

    def appendFile(self, filepath: str, filename: str):
        filename = self.ensure_pdf_extension(filename)
        pdfWriter = pypdf.PdfWriter()
        pdfReader = pypdf.PdfReader(self.totalFile)

        for page in range(len(pdfReader.pages)):
            pdfWriter.add_page(pdfReader.pages[page])

        additionalPdfPath = os.path.join(filepath, filename)
        additionalPdfReader = pypdf.PdfReader(additionalPdfPath)

        for page in range(len(additionalPdfReader.pages)):
            pdfWriter.add_page(additionalPdfReader.pages[page])

        with open(self.totalFile, "wb") as output_file:
            pdfWriter.write(output_file)

    def mergeFile(self, filepath: str, filename: str = None, outputPath: str = None, outputName: str = None):
        filename = self.ensure_pdf_extension(filename)
        pdfWriter = pypdf.PdfWriter()

        # Check if the initial file exists
        if not os.path.exists(self.totalFile):
            print(f"Error: The file {self.totalFile} does not exist.")
            return

        pdfReader = pypdf.PdfReader(self.totalFile)

        for page in range(len(pdfReader.pages)):
            pdfWriter.add_page(pdfReader.pages[page])

        # If no filename is provided, use the filename of the initial file
        if not filename:
            filename = os.path.basename(self.totalFile)

        # If no directory path is provided, use the directory of the initial file
        if not filepath:
            filepath = self.path

        additionalPdfPath = os.path.join(filepath, filename)

        # Check if the additional file exists
        if not os.path.exists(additionalPdfPath):
            print(f"Error: The file {additionalPdfPath} does not exist.")
            return

        additionalPdfReader = pypdf.PdfReader(additionalPdfPath)

        for page in range(len(additionalPdfReader.pages)):
            pdfWriter.add_page(additionalPdfReader.pages[page])

        # If no output path is provided, use the directory of the initial file
        if not outputPath:
            outputPath = self.path

        # If no output name is provided, use "merged_output.pdf"
        if not outputName:
            outputName = "merged_output.pdf"

        outputFilePath = os.path.join(outputPath, self.ensure_pdf_extension(outputName))

        with open(outputFilePath, "wb") as output_file:
            pdfWriter.write(output_file)

        print(f"Files merged successfully and saved to: {outputFilePath}")

    def mergeFiles(self, filepaths, outputPath: str, outputName: str):
        filepaths = [self.ensure_pdf_extension(f) for f in filepaths]

        # Add self.totalFile to filepaths if it exists
        if self.totalFile:
            filepaths.append(self.totalFile)

        pdfWriter = pypdf.PdfWriter()

        for filepath in filepaths:
            pdfReader = pypdf.PdfReader(filepath)
            for page in range(len(pdfReader.pages)):
                pdfWriter.add_page(pdfReader.pages[page])

        outputFilePath = os.path.join(outputPath, self.ensure_pdf_extension(outputName))

        with open(outputFilePath, "wb") as output_file:
            pdfWriter.write(output_file)

        print(f"Files merged successfully and saved to: {outputFilePath}")

    def searchFile(self, filepath: str, filename: str):
        filename = self.ensure_pdf_extension(filename)
        return os.path.exists(os.path.join(filepath, filename))

    def mergeFilesWithoutInternalFile(self, filepaths, outputPath: str, outputName: str):
        pdfWriter = pypdf.PdfWriter()

        for filepath in filepaths:
            pdfReader = pypdf.PdfReader(filepath)
            for page in range(len(pdfReader.pages)):
                pdfWriter.add_page(pdfReader.pages[page])

        outputFilePath = os.path.join(outputPath, self.ensure_pdf_extension(outputName))

        with open(outputFilePath, "wb") as output_file:
            pdfWriter.write(output_file)

        print(f"Files merged successfully and saved to: {outputFilePath}")

    def deleteFile(self, filepath: str, filename: str):
        filename = self.ensure_pdf_extension(filename)
        file_to_delete = os.path.join(filepath, filename)
        if os.path.exists(file_to_delete):
            os.remove(file_to_delete)
            return True
        return False

    def deleteExternalFile(self, filepath: str, filename: str):
        return self.deleteFile(filepath, filename)

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

        print(f"File split into:\n{part1}\n{part2}")

    def splitExternFile(self, filepath: str, filename: str, position: int, nameNewFile: str):
        filename = self.ensure_pdf_extension(filename)
        file_to_split = os.path.join(filepath, filename)

        pdfReader = pypdf.PdfReader(file_to_split)
        pdfWriter = pypdf.PdfWriter()

        for page in range(position, len(pdfReader.pages)):
            pdfWriter.add_page(pdfReader.pages[page])

        new_file_path = os.path.join(filepath, self.ensure_pdf_extension(nameNewFile))

        with open(new_file_path, "wb") as output_file:
            pdfWriter.write(output_file)

        print(f"File split successfully and saved to: {new_file_path}")

    def appendFileNameIncluded(self, filepath: str):
        filename = os.path.basename(filepath)
        dirPath = os.path.dirname(filepath)
        self.appendFile(dirPath, filename)

    @staticmethod
    def ensure_pdf_extension(filename: str):
        if not filename.endswith(".pdf"):
            filename += ".pdf"
        return filename
