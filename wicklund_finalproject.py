#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 16:32:11 2020

@author: DANI
"""
import json
import csv
import matplotlib.pyplot as plt

# Reads data from a file the user supplies. In this case, crime.csv
# This is also a menu driven program.
filename = "crime.csv"

#Displays a Crime report.
def crime_report():    
    
    counts = {}
    
    def ncic(ncic_count):
        with open(filename) as file:
            data_from_file = csv.reader(file)
            header_row = next(data_from_file)   
            ncic_count = []
            
        for row in data_from_file:
            temp = int(row[6])
            if temp < 1000:
                ncic_count[0] = ncic_count[0] +1
            elif temp >= 1000 and temp < 2000:
                ncic_count[1] = ncic_count[1] +1  
            elif temp >= 2000 and temp < 3000:
                ncic_count[2] = ncic_count[2] +1
            elif temp >= 3000 and temp < 4000:
                ncic_count[3] = ncic_count[3] +1
            elif temp >= 4000 and temp < 5000:
                ncic_count[4] = ncic_count[4] +1
            elif temp >= 5000 and temp < 6000:
                ncic_count[5] = ncic_count[5] +1
            elif temp >= 6000 and temp < 7000:
                ncic_count[6] = ncic_count[6] +1
            elif temp >= 7000 and temp < 8000:
                ncic_count[7] = ncic_count[7] +1
            elif temp >= 8000 and temp < 9000:
                ncic_count[8] = ncic_count[8] +1   
                
    def district():
        with open(filename) as file:
         data_from_file = csv.reader(file)
         header_row = next(data_from_file)   
         district_count = []
         
         for row in data_from_file:
             temp = int(row[6])
             if temp < 1:
                 district_count[0] = district_count[0] +1
             elif temp >= 1 and temp < 2:
                 district[1] = district[1] +1                   
             elif temp >= 2 and temp < 3:
                 district[2] = district[2] +1
                 district_count.append(temp)
             elif temp >= 3 and temp < 4:
                 district[3] = district[3] +1
                 district_count.append(temp)
             elif temp >= 4 and temp < 5:
                 district[4] = district[4] +1
                 district_count.append(temp)
             elif temp >= 5 and temp < 6:
                 district[5] = district[5] +1
                 district_count.append(temp)
             elif temp >= 6 and temp < 7:
                 district[6] = district[6] +1
                 district_count.append(temp)
                        
    def beat():
        with open(filename) as file:
            data_from_file = csv.reader(file)
            header_row = next(data_from_file)   
            beat_count = []    
    
        for row in data_from_file:
            temp = int(row[3])
            if temp < 1:
               beat_count[0] = beat_count[0] +1
            elif temp >= 1 and temp < 2:
                beat_count[1] = beat[1] +1   
            elif temp >= 2 and temp < 3:
                beat_count[2] = beat_count[2] +1
            elif temp >= 3 and temp < 4:
                beat_count[3] = beat_count[3] +1
            elif temp >= 4 and temp < 5:
                beat_count[4] = beat_count[4] +1
            elif temp >= 5 and temp < 6:
                beat_count[5] = beat_count[5] +1
            elif temp >= 6 and temp < 7:
                beat_count[6] = beat_count[6] +1
                
    counts['crimes'] = []
                
    counts['crimes'].append({
        'NCIC code': len('ncic_count'),
        'District': len('district_count'),
        'Beat': len('beat_count')
        })
    
    with open('October.json', 'w') as json_file:
        json.dump(counts,json_file)
        
    print(counts)
    
# Asks the user for a beat number and display all of the crimes (not the count!) for that beat sorted from lowest ncic number to highest
def display_beat():
    with open(filename) as file:
        data_from_file = csv.reader(file)
        header_row = next(data_from_file)   
        crimes = []
        print("Beat?")
        mybeat = input("==> ")
        
        for row in data_from_file:            
            CheckBeat = row[3]
            CheckBeat = CheckBeat.strip()
            if CheckBeat == mybeat:
                crimes.append(row[6] +"  " + row[5])

        crimes.sort()
        for crime in crimes:
            print(crime)
            
# Asks the user for 5 ncic numbers and create a bar chart of the count of those 5 ncic codes.
def ncic_chart():
    with open(filename) as file:
        data_from_file = csv.reader(file)
        header_row = next(data_from_file)   
        
    NCIC_code = []     
    NCIC_count = []
    
    status = True
    while status:
       print("\nPlease enter 5 ncic codes one by one.")
       print("\nEnter 'stop' to end the program.")
       message = input("Enter your desired code: ")
       NCIC_code.append(input)
       if message =='stop':
            status = False     
                        
    if (NCIC_code == message):
        for row in data_from_file:
            temp = int(row[6])
            if (temp == NCIC_code[0]): 
                NCIC_count[0] = NCIC_count[0] +1
            elif (temp == NCIC_code[1]):
                NCIC_count[1] = NCIC_count[1] +1
            elif (temp == NCIC_code[2]):
                NCIC_count[2] = NCIC_count[2] +1
            elif (temp == NCIC_code[3]):
                NCIC_count[3] = NCIC_count[3] +1
            elif (temp == NCIC_code[4]):
                NCIC_count[4] = NCIC_count[4] +1
            elif (temp == NCIC_code[5]):
                NCIC_count[5] = NCIC_count[5] +1
            elif (temp == NCIC_code[6]):
                NCIC_count[6] = NCIC_count[6] +1
            elif (temp == NCIC_code[7]):
                NCIC_count[7] = NCIC_count[7] +1
            elif (temp == NCIC_code[8]):
                NCIC_count[8] = NCIC_count[8] +1

    plt.bar(NCIC_count, NCIC_count, color='blue')
    plt.xticks(NCIC_count, NCIC_count)
    plt.xlabel("ucr_ncic_codes")
    plt.ylabel("Count")
    title_name=input('Please enter a title for the graph: ')
    plt.title(title_name)
    
    plt.savefig(title_name)
    
    plt.show()

cont = True
while cont:
    print("\tMenu\n")
    print("\t1. Print a report")
    print("\t2. Print stats for beat")
    print("\t3. Make a graph")
    print("\t4. Quit")
    user_input = input ("===>")
    if (user_input == '1'):
        print(crime_report())
    if (user_input == '2'):
        print(display_beat())
    if (user_input == '3'):
        ncic_chart()
#Quits the program.
    if (user_input == '4'):
        print("You have selected quit")
        cont = False