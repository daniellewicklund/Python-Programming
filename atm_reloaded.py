#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 14:42:19 2021

@author: pabudu
"""
from csv import reader
from math import floor


def verify_pin(account, pin):
    return account['pin'] == pin

def verify_acc(account):
    return users[account] if account in users else None

def save():
    with open("atm_fvr.csv", "w+") as csvFile:
        csvFile.write("Name ,Account Pin ,Balance\n")
        for user in users:
            csvFile.write(f"{user}, {users[user]['pin']}, {floor(users[user]['balance'])}\n")

def log_in():
    tries = 0
    account = None
    while tries < 4:
        while account == None:
            account = verify_acc(input('Please Enter Your Name: '))
            if(account == None):
                print("Invalid Name")
                tries += 1
                if(tries == 4):
                    return None
            else:
                tries = 0

        if verify_pin(account, input('Please Enter Your 4 Digit Pin: ')):
            print("Pin accepted!")
            return account
        else:
            print("Invalid pin")
            tries += 1
    print("To many incorrect tries. Could not log in")
    return None

def check_balance(account):
    print(f'Your Balance is £{account["balance"]}\n')

def withdraw(account):
    withdrawl = float(input('How Much Would you like to withdraw?\n£10/£20/£40/£60/£80/£100 for other enter 1: '))
    if withdrawl in [10, 20, 40, 60, 80, 100]:
        if(account['balance'] < withdrawl):
            print("Insufficient balance\n")
            return
        account['balance'] -= withdrawl
        save()
        check_balance(account)
    elif withdrawl == 1:
        withdrawl = float(input('Please Enter Desired amount:'))
        if(account['balance'] < withdrawl):
            print("Insufficient balance")
            return
        account['balance'] -= withdrawl
        save()
        check_balance(account)
    elif withdrawl != [10, 20, 40, 60, 80, 100]:
        print('Invalid Amount, Please Re-try')

def pay_in(account):
    Pay_in = float(input('How Much Would You Like To Pay In? '))
    account['balance'] += Pay_in
    save()
    check_balance(account)

def main_menu(account):
    while True:
        print('Please Press 1 To Check Balance')
        print('Please Press 2 To Make a Withdrawl')
        print('Please Press 3 To Deposit')
        print('Please Press 4 To Return Card and Exit')
        option = int(input('What Would you like to choose: '))
        if option == 1:
            check_balance(account)
        elif option == 2:
            withdraw(account)
        elif option == 3:
            pay_in(account)
        elif option == 4:
            print("Thank you for using  the atm")
            break

        restart = input('Would You you like to perform another transaction? (yes/no): ')
        if restart in ('n','NO','no','N'):
            print('Thank You')
            break

def new_account():
    name = input("Name: ")
    pin = ""
    while len(pin) != 4:
        pin = input("Enter 4 digit pin: ")

    users[name] = {'pin': pin, 'balance': int(input("Balance: "))}
    save()
    
def start_menu():
    print("Welcome to the atm!")
    option = ''
    while option != '0':
        option = input("New account 1 | Log in 2 | Quit 0: ")
        if option == '1':
            new_account()
            continue

        elif option == '2':
            account = log_in()
            if account != None:
                # you will need to make this one yourself!
                main_menu(account)
            break
    print("Exiting Program")



users = {}
with open("atm_fvr.csv", "r") as csvFile:
    csvreader = reader(csvFile)
    csvreader.__next__()
    for line in csvreader:
        users[line[0].strip()] = {'pin': line[1].strip(), 'balance': int(line[2])}

start_menu()