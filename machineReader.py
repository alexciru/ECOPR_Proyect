from io import *

class MachineReader:

    def __init__(self):
        self.document = None
        return

    def readFile(self, file):
        self.document = open(file, "r")
        info = self.document.readlines()
        for i in info:
            for j in i:
                if j > 0 


        #print(info)
        return
