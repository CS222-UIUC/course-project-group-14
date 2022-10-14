import re
import csv
import os

def mergeList(list1, list2, merged_list):
    for n in (list1, list2):
        for x in n:
            merged_list.append(x)
            
def FindingDates(file, output):
    with open(file, 'r') as f:
        for line in f:
            #parse
            merge1_list = []
            merge2_list = []
            merge3_list = []
            merge_week_list = []
            final_list = []
            add_time_list = []
            week_am_pm_list = []
            ist_list = []
            not_february_ist_list = []
            time_list = []
            not_february_time_list = []
            timeist_list = []
            
            
            theMonthOf_list = re.findall("(\sthe\s)(1st|2nd|3rd|[4-9]th|21st|22nd|23rd|2[04-9]th|1[0-9]th|30th|31st)(\sof\s)(January|February|March|April|May|June|July|August|September|October|November|December)(,\s\d{4})?", line)                  
            
            thirtyone_ist_list = re.findall("(Monday,\s|Tuesday,\s|Wednesday,\s|Thursday,\s|Friday,\s|Saturday,\s|Sunday,\s)?(January|March|May|July|August|October|December)(\s1st|\s2nd|\s3rd|\s[4-9]th|\s21st|\s22nd|\s23rd|\s2[04-9]th|\s1[0-9]th|\s30th|\s31st)?(, \d{4})?", line)
            thirty_ist_list = re.findall("(Monday,\s|Tuesday,\s|Wednesday,\s|Thursday,\s|Friday,\s|Saturday,\s|Sunday,\s)?(April|June|September|November)(\s1st|\s2nd|\s3rd|\s[4-9]th|\s21st|\s22nd|\s23rd|\s2[04-9]th|\s1[0-9]th|\s30th)?(, \d{4})?", line)
            feb_ist_list = re.findall("(Monday,\s|Tuesday,\s|Wednesday,\s|Thursday,\s|Friday,\s|Saturday,\s|Sunday,\s)?(February)(\s1st|\s2nd|\s3rd|\s[4-9]th|\s21st|\s22nd|\s23rd|\s2[04-9]th|\s1[0-9]th)?(, \d{4})?", line)
            
            mergeList(thirtyone_ist_list, thirty_ist_list, not_february_ist_list)
            mergeList(feb_ist_list, not_february_ist_list, ist_list)
            thirtyone_time_list = re.findall("(January|March|May|July|August|October|December)(\s[0-9]|\s1[0-9]|\s2[0-9]|\s3[0-1])(, \d{4})", line)
            thirty_time_list = re.findall("(April|June|September|November)(\s[0-9]|\s1[0-9]|\s2[0-9]|\s30)(, \d{4})", line)
            feb_time_list = re.findall("(February)(\s[0-2]?[0-9]?)(, \d{4})", line)
            
            mergeList(thirtyone_time_list, thirty_time_list, not_february_time_list)
            mergeList(feb_time_list, not_february_time_list, time_list)

            with open(output, 'w') as file:
                writer = csv.writer(file)
                writer.writerow(thirtyone_time_list)
            

#FindingDates('input.csv', 'test.csv')