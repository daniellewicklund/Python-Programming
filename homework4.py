#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 15:54:27 2020

@author: DANI
"""

import csv
import matplotlib.pyplot as plt
filename = "crime.csv"
with open(filename) as file:
    data_from_file = csv.reader(file)
    header_row = next(data_from_file)
    

    ucr_ncic_code = [0,1,2,3,4,5,6,7,8]
    for row in data_from_file:
        temp = int(row[6])
        if temp < 1000:
            ucr_ncic_code[0] = ucr_ncic_code[0] +1
        elif temp >= 1000 and temp < 2000:
            ucr_ncic_code[1] = ucr_ncic_code[1] +1   
        elif temp >= 2000 and temp < 3000:
            ucr_ncic_code[2] = ucr_ncic_code[2] +1
        elif temp >= 3000 and temp < 4000:
            ucr_ncic_code[3] = ucr_ncic_code[3] +1
        elif temp >= 4000 and temp < 5000:
            ucr_ncic_code[4] = ucr_ncic_code[4] +1
        elif temp >= 5000 and temp < 6000:
            ucr_ncic_code[5] = ucr_ncic_code[5] +1
        elif temp >= 6000 and temp < 7000:
            ucr_ncic_code[6] = ucr_ncic_code[6] +1
        elif temp >= 7000 and temp < 8000:
            ucr_ncic_code[7] = ucr_ncic_code[7] +1
        elif temp >= 8000 and temp < 9000:
            ucr_ncic_code[8] = ucr_ncic_code[8] +1   
  

labels = ('0-999', '1000-1999', '2000-2999', '3000-3999', '4000-4999', '5000-5999', '6000-6999', '7000-7999', '8000-8999')
#sizes = [15, 30, 45, 10] 
colors = ['lavender', 'yellowgreen', 'lightskyblue', 'lightgray', 'mediumpurple', 'lightcoral', 'tan', 'gold', 'lightpink']
explode = (0.75,0.0,0.0,0.0,0.6,0.0,0.95,0.0,0.95)  
fig1,ax1 = plt.subplots()
#axis are the individual pie pieces
ax1.pie(ucr_ncic_code, explode = explode,labels = labels, colors = colors, autopct='%1.1f%%', shadow=True, startangle=70)

ax1.axis('equal') 
plt.savefig('myplot')
plt.show()            