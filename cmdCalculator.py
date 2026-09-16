def plus():
    num1 = (input("Give the first Number: "))
    while num1.isdigit() == False:
        num1 = (input("\033[31mYou didn't typed a valid Number. Try again:\033[0m "))

    num2 = (input("Give the second Number: "))
    while num2.isdigit() == False:
        num2 = (input("\033[31mYou didn't typed a valid Number. Try again:\033[0m "))
    
    num1 = float(num1)
    num2 = float(num2)

    result = num1 + num2

    print("------------------------------------------------------------------------")
    print(f"The result is '{result}'.")


def minus():
    num1 = (input("Give the first Number: "))
    while num1.isdigit() == False:
        num1 = (input("\033[31mYou didn't typed a valid Number. Try again:\033[0m "))

    num2 = (input("Give the second Number: "))
    while num2.isdigit() == False:
        num2 = (input("\033[31mYou didn't typed a valid Number. Try again:\033[0m "))
    
    num1 = float(num1)
    num2 = float(num2)

    if num1 > num2:
        result = num1 - num2

    else:
        result = num2 - num1

    print("------------------------------------------------------------------------")
    print(f"The result is '{result}'.")

    
def multiply():
    num1 = (input("Give the first Number: "))
    while num1.isdigit() == False:
        num1 = (input("\033[31mYou didn't typed a valid Number. Try again:\033[0m "))

    num2 = (input("Give the second Number: "))
    while num2.isdigit() == False:
        num2 = (input("\033[31mYou didn't typed a valid Number. Try again:\033[0m "))
    
    num1 = float(num1)
    num2 = float(num2)

    result = num1 * num2


    print("------------------------------------------------------------------------")
    print(f"The result is '{result}'.") 


def divide():
    num1 = (input("Give the first Number: "))
    while num1.isdigit() == False:
        num1 = (input("\033[31mYou didn't typed a valid Number. Try again:\033[0m "))

    num2 = (input("Give the second Number: "))
    while num2.isdigit() == False:
        num2 = (input("\033[31mYou didn't typed a valid Number. Try again:\033[0m "))
    
    num1 = float(num1)
    num2 = float(num2)

    if num1 > num2:
        result = num1/num2

    else:
        result = num2/num1

    print("------------------------------------------------------------------------")
    print(f"The result is '{result}'.")    


print("------------------------------------------------------------------------")
print("Welcome to an Calculator coded with Python.")
print("Just follow the steps.")
print("At the moment you can only add 2 numbers.")
print("Also you can't go in the '-' Area at the moment.")
print("------------------------------------------------------------------------")


while True:

    print("Chose, which Math you want to use: ")
    print("+ for plus")
    print("- for minus")
    print("* for multiply")
    print("/ for divide")
    chose = input("Chose: ")
    print("------------------------------------------------------------------------")

    if chose == "+":
        plus()
    elif chose == "-":
        minus()
    elif chose == "*":
        multiply()
    elif chose == "/":
        divide()
    else:
        print("\033[31mDid you really chose a allowed Math? Try again:\033[0m ")
        print("------------------------------------------------------------------------")
        continue

        
    yn = input("Do you want to make a other calculation? Yes / No: ").lower()

    if yn == "yes":
        print("You chose Yes.")
        print("------------------------------------------------------------------------")
        continue
    elif yn == "no":
        print("You chose No")
        break
    else:
        print(f"You typed '{chose}'. The Programm doesn't know that.")
        yn = input("Do you want to try again Yes / No: ").lower()

input("Press Enter to Exit...")
