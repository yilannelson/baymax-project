import time
from os import system, name

def clear(): 
        system('clear') 

def main_menu():
    clear()
    print("-----------------------------------\n"
          "What sypmtoms are you displaying?\n"
          "-----------------------------------\n"
          "[1] Runny Nose\n"
          "[2] Sore Throat\n"
		  "[3] Dehydration\n"
          "[4] Other\n"
          "Select option 4 for other symptoms ")

def idle_screen():
    clear()
    print("Hello I am Baymax, your personal healthcare companion. \nI offer personalized solutions for your medical needs so you can become healthy!\n"
          "Press any button to begin!")
    choice = input("")
    choice = str(choice)
    if choice == "e":
        return main_menu()
    else:
        return main_menu()

def vend_complete():
    print("Have a nice Day")
    time.sleep(5)
    return idle_screen()

def runny_nose():

    while True:
        clear()
        print("-----------------------------------\n"
          "Runny Nose menu:\n"
          "-----------------------------------\n"
          "[1] Tissue    \n"
                                                 )
        choice = input("Runny Nose option: ")
        choice = str(choice)
        if choice == "1":
            global balance
            balance = float(balance) - 1
            global total_purchase
            print("Vending tissues, have a nice day")
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
def dehydration

	while True:
        clear()
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
            print("Vending tissues, have a nice day")
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
          "Cough Drops\n")
        choice = input("Sore Throat option: ")
        choice = str(choice)
        if choice == "Cough Drops":
            global balance
            balance = float(balance) - 0.99
            global total_purchase
            if(balance >0):
                print("Vending water, you have", str(balance), "dollars left")
            else:
                print("you don't have enough money to buy Chips <", str(rdollar), "<", str(0.99), ">")

while True:
    idle_screen()
    choice = input()
    choice = int(choice)
    if choice == 1:
            balance = 1
            runny_nose()
    elif choice == 2:
            balance = 2
            SoreThroat_menu()
    elif choice == 3:
            balance = 3
            other()
    elif choice == 4:
            print("-------------------------------\n"
                  "Inserted amount: ", str(rdollar),",", "total purchase: ", rdollar-balance, ",", "change: ", balance)
            exit()
    else:
            print("invalid option!")
@app.route('/hello/')

