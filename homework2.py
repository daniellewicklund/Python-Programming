#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 15:34:23 2020

@author: DANI
"""
name_list = ['Dora', 'Popeye', 'Shaggy']

number_list= []

def get_store_name():
    """Has a function that asks the user for their first name and stores it to a list."""
    name_list.append(user_input)
            
def get_store_number():
    """Has a function that selects a random number for each name and adds it to a second list."""
    import random
    random.seed()
    # From inside that function, get a random number between 1 and 10.
    name_list = random.sample(range(1,10),4)
    for i in range (4):
        number_list.append(name_list)
    # The random number is generated in its own function.
    print("These are your random numbers: "+str(number_list[1]))

def both_lists(name_list,number_list):
    """Has a function that prints out both lists in the specified format."""
    index1 = name_list.index('Dora')
    index2 = name_list.index('Popeye')
    index3 = name_list.index('Shaggy')
    index4 = name_list.index(user_input)
    for name, number in zip(name_list,number_list):
        print('Dora',"-",number[index1])
        print('Popeye',"-",number[index2])
        print('Shaggy',"-",number[index3])
        print(user_input,"-",number[index4])
        return
        
def single_value(user_input,number_list):
   """Has a function that only prints a single name and number."""
   index = name_list.index(user_input)
   # This function receives the name and does not ask for it inside the function.
   for user, number in zip(user_input,number_list):
        print(user_input)
        print(number[index])
        return

user_input=input("Please enter your first name: ")
get_store_name()

input("Please enter to generate a random numbers: ")
get_store_number()

input("Please enter to view all names and numbers: ")
both_lists(name_list,number_list)

input("Please enter to view a single name and number: ")
single_value(user_input,number_list)

# The program is menu driven.