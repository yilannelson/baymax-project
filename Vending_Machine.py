import time
def main_menu():
    print("-----------------------------------\n"
          "Main menu:\n"
          "-----------------------------------\n"
          "[1] Runny Nose\n"
          "[2] Sore Throat\n"
          "[3] Other\n"
          "Select option 3 to exit>: ")

def idle_screen():
    print("Welcome to the Baymax Vending Machine!\n"
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
        print("-----------------------------------\n"
          "Runny Nose menu:\n"
          "-----------------------------------\n"
          "[1] Tissue    \n"
          "[2] Juice    \n"
          "[3] Soda     \n"
          "Select a drink by entering the number next to the name <x to exit to the main menu>\n")

        choice = input("Drink option: ")
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

def snacks_menu():

    while True:
        print("-----------------------------------\n"
          "snacks menu:\n"
          "-----------------------------------\n"
          "Chips    $0.99\n"
          "Peanuts  $0.5\n"
          "Gum      $1.35\n"
          "Select a snack by entering the full name <x to exit to the main menu>\n")

        choice = input("Snack option: ")
        choice = str(choice)
        if choice == "Chips":
            global balance
            balance = float(balance) - 0.99
            global total_purchase
            if(balance >0):
                print("Vending water, you have", str(balance), "dollars left")
            else:
                print("you don't have enough money to buy Chips <", str(rdollar), "<", str(0.99), ">")

        elif choice == "Peanuts":
            balance = float(balance) - 0.5
            if(balance >0):
                print("Vending Juice, you have", str(balance), "dollars left")
            else:
                print("you don't have enough money to buy Peanuts <", str(rdollar), "<", str(0.5), ">")
        elif choice == "Gum":
            balance = float(balance) - 0.35
            if(balance >0):
                print("Vending Gum, you have", str(balance), "dollars left")
            else:
                print("you don't have enough money to buy Gum <", str(rdollar), "<", str(0.35), ">")
        elif choice == "x":
            return main_menu()
        else:
            print("invalid option!")

while True:

    idle_screen()
    choice = input()
    choice = int(choice)
    if choice == 1:
            balance = 1
            runny_nose()
    elif choice == 2:
            balance = 2
            snacks_menu()
    elif choice == 3:
            print("-------------------------------\n"
                  "Inserted amount: ", str(rdollar),",", "total purchase: ", rdollar-balance, ",", "change: ", balance)
            exit()
    else:
            print("invalid option!")
