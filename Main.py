from bs4 import BeautifulSoup
import pprint
import csv
from Extractor import Extractor



class Main:
    
    def extractToCSV(inputDir, outputDir):
        Extractor.exportFromDicToCSV(Extractor.extractFromXmlToDictionary(inputDir), outputDir)

    if __name__ == "__main__":
        decision = input ("Do you want the output to be a .csv with the corresponding word frequency (1) or an Anki compatible file with a translation (2)? \nPlease enter only the corresponding number: ")
        

        if (decision == "1"):
            inputDir = input("Please enter the file path to the xml subtitle file: ")
            outputDir = input("Please enter the file path you want the new .csv file to be at: ")
            extractToCSV(inputDir, outputDir)
        elif (decision == "2"):
            inputDir = input("Please enter the file path to the xml subtitle file: ")
            outputDir = input("Please enter the file path you want the new Anki compatible file to be at: ")
            Extractor.extractToAnki(inputDir, outputDir)
        else:
            print("You are only allowed to enter '1' or '2'")