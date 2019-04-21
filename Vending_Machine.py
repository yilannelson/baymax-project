from flask import Flask, render_template
from __init__ import *
def buttons():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Dispense Wet Wipes':
            print("Wet Wipes")
        elif request.form['submit_button'] == 'Dispense Cough Drop':
            print("Cough Drop")
        elif request.form['submit_button'] == 'Dispense Herbal Tea': 
            print("Tea")
        elif request.form['submit_button'] == 'Dehydration':
            return dehydrationhtml()
        else:
            pass 
@app.route("/dehydration")
def dehydrationhtml():
    return render_template("/dehydration/index.html")
@app.route("/sore_throat")
def sthroathtml():
    return render_template("/sore_throat/index.html")
@app.route("/none")
def nonehtml():
    return render_template("/none/index.html")
@app.route("/other")
def otherhtml():
    return render_template("/other/index.html")

@app.route('/')
def hello():
    return render_template('index.html')
	
if __name__ == '__main__':
    app.run(debug=True)
import time
from os import system, name

def clear(): 
        system('cls') 

def main_menu():
    clear()
    print("-----------------------------------\n"
          "What sypmtoms are you displaying?\n"
          "-----------------------------------\n"
          "[1] None\n"
          "[2] Sore Throat\n"
		  "[3] Dehydration\n"
          "[4] Other\n"
          "Select option 4 for other symptoms ")

def idle_screen():
        clear()
        print("Hello I am Baymax, your personal healthcare companion. \nI offer personalized solutions for your medical needs so you can become healthy!\n"
          "Press any button to begin!")
        choice = input()
        choice = str(choice)
        if choice == 1:
            return main_menu()
        else:
            return main_menu()
        return idle_screen()
def vend_complete():
    print("Have a nice Day")
    time.sleep(5)
    return idle_screen()

def none():

    while True:
        clear()
        print("-----------------------------------\n"
          "none menu:\n"
          "-----------------------------------\n"
          "[1] Wet Wipes    \n"
                                                 )
        choice = input("none option: ")
        choice = str(choice)
        if choice == "1":
            global balance
            balance = float(balance) - 1
            global total_purchase
            print("Vending Wet Wipes, have a nice day")
            return vend_complete()
        elif choice == "2":
            balance = float(balance) - 1
            print("Vending Juice")
            return vend_complete()
        elif choice == "3":
            balance = float(balance) - 1
            print("Vending Soda")
            return vend_complete()
        elif choice == "x":
            return main_menu()
        else:
            print("invalid option!")

def dehydration():

    while True:
        system('cls')
        print("-----------------------------------\n"
          "Dehydration menu:\n"
          "-----------------------------------\n"
          "[1] Herbal Tea    \n"
                                                 )
        choice = input("Dehydration option: ")
        choice = str(choice)
        if choice == "1":
            global balance
            balance = float(balance) - 1
            global total_purchase
            print("Vending Herbal Tea, have a nice day")
            return vend_complete()
        elif choice == "2":
            balance = float(balance) - 1
            print("Vending Juice")
            return vend_complete()
        elif choice == "3":
            balance = float(balance) - 1
            print("Vending Soda")
            return vend_complete()
        elif choice == "x":
            return main_menu()
        else:
            print("invalid option!")
		
def other():

    while True:
        clear()
        print("------------------------------------ \n" 
          "Other Symptoms:\n"
          "------------------------------------ \n"
          "We are unable to assist you with your symptoms, we advise going to see the school nurse for aditional assitance\n")
def SoreThroat_menu():

    while True:
        clear()
        print("-----------------------------------\n"
          "Sore Throat menu:\n"
          "-----------------------------------\n"
          "[1] Cough Drops\n")
        choice = input("Sore Throat option: ")
        choice = str(choice)
        if choice == "Cough Drops":
            global balance
            balance = float(balance) - 0.99
            global total_purchase
            if(balance >0):
                print("Vending cough drops, you have", str(balance), "dollars left")
            else:
                print("you don't have enough money to buy Chips <", str(rdollar), "<", str(0.99), ">")

while True:
    idle_screen()
    choice = input()
    choice = int(choice)
    if choice == 1:
            balance = 1
            none()
    elif choice == 2:
            balance = 2
            SoreThroat_menu()
    elif choice == 3:
            balance = 3
            dehydration()
	#elif choice == 5:
     #       balance = 5
      #      other()
    elif choice == 4:
            print("Work in Progress.\n")
            exit()
    elif choice == string:
            main_menu()
    else:
            print("invalid option!")
