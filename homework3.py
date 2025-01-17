#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 21:38:58 2020

@author: DANI
"""
import matplotlib.pyplot as graph

high_temps = [46.6, 46.9, 50.4, 53.8, 58.6, 63.7, 67.1, 66.6, 62.6, 56.5, 50.5, 46.9]
twelve_months = ["Jan.","Feb.","Mar.","Apr.","May","June","Jul.", "Aug.", "Sept.", "Oct.", "Nov.", "Dec."]
graph.title("Average High Temperatures for Each Month in Dublin",fontsize = 14)
graph.xlabel("Months",fontsize = 12)
graph.ylabel("Temperature (°F)",fontsize = 12)
graph.tick_params(axis='both',labelsize = 12)
graph.plot(twelve_months,high_temps, color="g")
graph.show()

import matplotlib.pyplot as graph

avg_temp = [41.5, 41.5, 44.2, 46.9, 51.6, 56.5, 60.1, 59.5, 56.1, 50.9, 45.3, 42.1]
avg_precip = [2.46, 1.92, 2.07, 2.13, 2.34, 2.63, 2.21, 2.89, 2.34, 3.11, 2.87, 2.86]
graph.title("Average Temperature vs Average Rainfall Each Month in Dublin",fontsize = 14)
graph.xlabel("Temperature (°F)",fontsize = 12)
graph.ylabel("Average precipitation (Inches)",fontsize = 14)
graph.tick_params(axis='both',labelsize = 12)
graph.scatter(avg_temp,avg_precip,c='orange',edgecolor='green',s=10)
graph.show()

import matplotlib.pyplot as plt
relative_percentages = [60, 20, 20]
dif_categories = ('4 Projects', '1 Project', '1 Exam')
explode = (0.0, 0.3, 0.0)  
# The Project: slice is exploded from the rest of the pie.
fig1,ax1 = plt.subplots()
ax1.pie(relative_percentages, explode = explode,labels = dif_categories, autopct='%1.0f%%', shadow=True, startangle=45)
ax1.axis('equal') 
ax1.set_title("Different categories of grades in this class and their relative percentage of the final grade")
plt.show()