import re
import csv

import os
import PyPDF2
import pandas as pd

def ReadPDF(): # function that reads/outputs entire pdf file for parsing
    print("HERE")
    pdfFile = open('Main/Frontend/static/file.pdf', 'rb') 
    pdfReader = PyPDF2.PdfReader(pdfFile)
    numPages = len(pdfReader.pages)

    # txt file we write to in order to parse
    txtFile = open("Main/Backend/parsed.txt", "a")

    # clears previous entry
    with open("Main/Backend/parsed.txt", 'w') as o:
        o.write("")

    for i in range(0, numPages): # read entire file
        txtFile.write(pdfReader.getPage(i).extract_text())
        txtFile.write("\n\n")

    pdfFile.close()
    txtFile.close()

def mergeList(list1, list2, merged_list):
    for n in (list1, list2):
        for x in n:
            merged_list.append(x)
            

def FindingDates():
    i = 0
    midterm_list = []
    slash_date_list = []
    test_list = ["March 3", "December 24", "Midterm"]

    file1 = open("Main/Backend/parsed.txt", 'r')
    lines = file1.readlines()
    for line in lines:
        cal = []
        word = ["calendar"]
        pattern = r'\W.*?({})\W.*?'.format('|'.join(word))
        cal = re.findall(pattern, line, flags=re.IGNORECASE)
        if len(cal) != 0:
            break
        i+=1
    for line in lines:
        #parse
        if i == 0:
            #word1 = ["midterm"]
            #pattern1 = r'\W.*?({})\W.*?'.format('|'.join(word1))
            #midterm = re.findall(pattern1, line, flags=re.IGNORECASE)
            #if len(midterm) != 0:
             #   midterm_list.append(midterm)

            pattern= [r'\D+']
            for j in pattern:
                midterm= re.findall(j, line)
                midterm_list.append(midterm)
            
            # begin with 1-31 followed by slash, followed by 1-12
            # slash_date_list = re.findall("^([1-9] |1[0-9]| 2[0-9]|3[0-1])/([1-9] |1[0-2])$", line, flags=re.IGNORECASE)
            slash_date_pattern = re.compile('\\b((0[1-9]|1[0-2]|[1-9])/([1-9]|0[1-9]|[1-2][0-9]|3[0-1]))\\b')
            slash_dates = slash_date_pattern.findall(line)
            if len(slash_dates) != 0:
                slash_date_list.append(slash_dates)
            continue
        i-=1
    #Subject,Start Date,Start Time,End Date,End Time,All Day Event,Description,Location,Private
    findlist = []
    file = open("Main/Backend/result.csv", 'w')
    writer = csv.writer(file)
    findlist.append(midterm_list[0][0])
    findlist.append(slash_date_list[0][0][0])
    writer.writerow(findlist)
    writer.writerow(midterm_list)
    writer.writerow(slash_date_list)
            

