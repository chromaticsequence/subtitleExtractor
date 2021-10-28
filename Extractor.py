from bs4 import BeautifulSoup
import pprint
import csv

class Extractor:
    # Reading the data inside the xml
    # file to a variable under the name
    # data

    #inputDir = '0XXYtL9X.xml'
    #outputDir = 'd2.csv'
    #outputDir = inputDir + ".csv"

    def extractFromXmlToDictionary(inputDir):
        with open(inputDir, encoding='utf-8') as f:
            soup = BeautifulSoup(f,'lxml-xml',from_encoding='utf-8')


            #print(soup.get_text().strip())

            def word_count(str):
                counts = dict()
                words = str.split()

                for word in words:
                    if word in counts:
                        counts[word] += 1
                    else:
                        counts[word] = 1

                return counts

            output = word_count(soup.get_text().replace("]", "").replace("[", "").replace("—", "").replace("!", "").replace("?", "").replace(".", "").replace(",", "").strip())
            #print(output)
        
        return output

    def incOrder(input):
        return sorted(input.items(), key=lambda x: x[1]) #for inceasing order

    def printDicNicely(dic):
    # Ab hier pprint

        # Prints the nicely formatted dictionary
        pprint.pprint(dic)


        # Sets 'pretty_dict_str' to the formatted string value
        pretty_dict_str = pprint.pformat(dic)

    def exportFromDicToCSV(dictionary, outputDir):

    #ab hier csv
        with open(outputDir, 'w', encoding='utf8') as csv_file:  
            writer = csv.writer(csv_file)
            for key, value in dictionary.items():
                writer.writerow([key, value])
    
#    def exportFromDicToAnki(dictionary, outputDir):
    
#        for key, value in dictionary.items():
            # do something with value

#            dictionary[key] = newvalue

    #ab hier csv
#        with open(outputDir, 'w', encoding='utf8') as csv_file:  
#            writer = csv.writer(csv_file)
#            for key, value in dictionary.items():
#                writer.writerow([key, value])"

