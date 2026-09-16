print("------------------------------------------------------------------------")
print("Welcome to an Calculator coded with Python.")
print("Just follow the steps.")
print("At the moment you can only add 2 numbers.")
print("------------------------------------------------------------------------")



def plus():
    num1 = float(input("Give the first Number: "))
    num2 = float(input("Give the second Number: "))

    result = num1 + num2

    print("------------------------------------------------------------------------")
    print(f"The result is '{result}'.")

 

def multiply():
    num1 = float(input("Give the first Number: "))
    num2 = float(input("Give the second Number: "))

    result = num1 * num2

    print("------------------------------------------------------------------------")
    print(f"The result is '{result}'.") 



def minus():
    num1 = float(input("Give the first Number: "))
    num2 = float(input("Give the second Number: "))

    if num1 > num2:
        result = num1 - num2

    else:
        result = num2 - num1

    print("------------------------------------------------------------------------")
    print(f"The result is '{result}'.")


def divide():
    num1 = float(input("Give the first Number: "))
    num2 = float(input("Give the second Number: "))

    if num1 > num2:
        result = num1/num2

    else:
        result = num2/num1

    print("------------------------------------------------------------------------")
    print(f"The result is '{result}'.")    



while True:

    print("Chose, how you want to calculate:")
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
        print("Did you really chose a allowed Math?")
        yn = input("Do you want to try again? Yes / No: ").lower()

        if yn == "yes":
            print("You chose Yes.")
            print("------------------------------------------------------------------------")
            continue
        elif yn == "no":
            print("You chose No")
            print("Programm ended.")
            break
        else:
            print(f"You typed '{chose}'. The Programm doesn't know that.")
            print("Programm ended")
            break
        
    yn = input("Do you want to make a other calculation? Yes / No: ").lower()

    if yn == "yes":
        print("You chose Yes.")
        print("------------------------------------------------------------------------")
        continue
    elif yn == "no":
        print("You chose No")
        print("Programm ended.")
        break
    else: #genauer anschauen
        print(f"You typed '{chose}'. The Programm doesn't know that.")
        yn = input("Do you want to try again Yes / No: ").lower()


