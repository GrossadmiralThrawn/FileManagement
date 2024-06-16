class STDFileInterface:
    #Smart setter which should check th path name of the given data for syntactical correctness
    def setFile(self, filepath: str, fileName: str):
        pass

    #Deletes a file given in the parameter.
    def deleteExternFile(self, filepath: str, fileName: str):
        pass

    #Deletes the file which ist stored locally
    def deleteFile(self):
        pass

    #Returns the name of the File which ist stored into the class data
    def getFile(self):
        pass

    #Prints the address of the actual instance, and all local data
    def printData(self):
        pass

    #Divids a given file at 50% of it's size
    def splitExternFile(filepath: str, fileName: str, nameNewFile):
        pass

    #Divids the local file at 50% of its size at a selected position and gives a selected name.
    def splitFile(self, position: int):
        pass

    #append an external file with a finished variable
    def appendFileNameIncluded(filepath: str):
        pass

    #Append an external file, ut with two combine variables (less vulnerable)
    def appendFile(self, filepath: str, fileName: str):
        pass

    #Merges te local file with an external one and put the output file at awished position and with the requested file name
    def mergeFile(self, filepath: str, fileName: str , outputPath: str, outputName: str):
        pass


    #Merges many files with the internal File
    def mergeFiles(self, filepaths, outputPath: str, outputName: str):
        pass

    #Merges many files without the internal file
    def mergeFilesWithoutInternalFile(self, filepaths, outputPath: str, outputName: str):
        pass

    #Searchs for a file and returns a boolean
    def searchFile(filepath: str, fileName: str):
        pass
