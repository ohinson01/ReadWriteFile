'''
Program: Read and Write to a file
Date: 6/4/2020

Maintenance History:
    6/4/2020 - Create program
'''
'''
Read and write from existing file on results of user input
'''
from csv import reader

#create a variable for a file name 
filename = r"<Enter file path here>\Accidental_Drug_Related_Deaths_2012-2018.csv"

#prompt user for "key" field 
column = input("Please enter an ID you would like to retrieve from the file: ")

try:
    #iterate over each line as ordered dictionary and write only few columns by column number
    #open file in read mode
    with open(filename, "r") as inputFile:
        with open("results.txt", "wt") as outputFile:
            csv_reader = reader(inputFile)
            for row in csv_reader:
                if(row[0] == column):
                    outputFile.write(str(row))
                elif(row[1] == column):
                    outputFile.write(str(row))
                elif(row[2] == column):
                    outputFile.write(str(row))
                elif(row[3] == column):
                    outputFile.write(str(row))
                elif(row[4] == column):
                    outputFile.write(str(row))
                elif(row[5] == column):
                    outputFile.write(str(row))
                elif(row[6] == column):
                    outputFile.write(str(row))
                elif(row[7] == column):
                    outputFile.write(str(row))
                elif(row[8] == column):
                    outputFile.write(str(row))
                elif(row[9] == column):
                    outputFile.write(str(row))
except FileNotFoundError:
    print("The file you are trying to use is not available. Please enter a valid file path...")
finally:
    inputFile.close() #close inputFile 
    outputFile.close() #close outputfile
print("Done")




    
