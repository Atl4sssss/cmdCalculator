def plus():

    if chose_language == "English":
        num1 = (input("Enter the first Number: "))
        while num1.isdigit() == False:
            num1 = (input("\033[31mYou didn't typed a valid Number. Try again:\033[0m "))

        num2 = (input("Enter the second Number: "))
        while num2.isdigit() == False:
            num2 = (input("\033[31mYou didn't typed a valid Number. Try again:\033[0m "))
        
        num1 = float(num1)
        num2 = float(num2)

        result = num1 + num2

        print("------------------------------------------------------------------------")
        print(f"The result is '{result}'.")

    elif chose_language == "Deutsch":
        num1 = (input("Gebe die erste Nummer ein: "))
        while num1.isdigit() == False:
            num1 = (input("\033[31mDu hast keine erlaubte Nummer eingegeben. Probiere es nochmal:\033[0m "))

        num2 = (input("Gebe die zweite Nummer: "))
        while num2.isdigit() == False:
            num2 = (input("\033[31mDu hast keine erlaubte Nummer eingegeben. Probiere es nochmal:\033[0m "))
        
        num1 = float(num1)
        num2 = float(num2)

        result = num1 + num2

        print("------------------------------------------------------------------------")
        print(f"Das Resultat ist '{result}'.")


def minus():

    if chose_language == "English":
        num1 = (input("Enter the first Number: "))
        while num1.isdigit() == False:
            num1 = (input("\033[31mYou didn't typed a valid Number. Try again:\033[0m "))

        num2 = (input("Enter the second Number: "))
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

    elif chose_language == "Deutsch":
        num1 = (input("Gebe die erste Nummer ein: "))
        while num1.isdigit() == False:
            num1 = (input("\033[31mDu hast keine erlaubte Nummer eingegeben. Probiere es nochmal:\033[0m "))

        num2 = (input("Gebe die zweite Nummer: "))
        while num2.isdigit() == False:
            num2 = (input("\033[31mDu hast keine erlaubte Nummer eingegeben. Probiere es nochmal:\033[0m "))
        
        num1 = float(num1)
        num2 = float(num2)

        if num1 > num2:
            result = num1 - num2

        else:
            result = num2 - num1

        print("------------------------------------------------------------------------")
        print(f"Das Resultat ist '{result}'.")


def multiply():

    if chose_language == "English":
        num1 = (input("Enter the first Number: "))
        while num1.isdigit() == False:
            num1 = (input("\033[31mYou didn't typed a valid Number. Try again:\033[0m "))

        num2 = (input("Enter the second Number: "))
        while num2.isdigit() == False:
            num2 = (input("\033[31mYou didn't typed a valid Number. Try again:\033[0m "))
        
        num1 = float(num1)
        num2 = float(num2)

        result = num1 * num2

        print("------------------------------------------------------------------------")
        print(f"The result is '{result}'.")

    elif chose_language == "Deutsch":
        num1 = (input("Gebe die erste Nummer ein: "))
        while num1.isdigit() == False:
            num1 = (input("\033[31mDu hast keine erlaubte Nummer eingegeben. Probiere es nochmal:\033[0m "))

        num2 = (input("Gebe die zweite Nummer: "))
        while num2.isdigit() == False:
            num2 = (input("\033[31mDu hast keine erlaubte Nummer eingegeben. Probiere es nochmal:\033[0m "))
        
        num1 = float(num1)
        num2 = float(num2)

        result = num1 * num2

        print("------------------------------------------------------------------------")
        print(f"Das Resultat ist '{result}'.")


def divide():

    if chose_language == "English":
        num1 = (input("Enter the first Number: "))
        while num1.isdigit() == False:
            num1 = (input("\033[31mYou didn't typed a valid Number. Try again:\033[0m "))

        num2 = (input("Enter the second Number: "))
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

    elif chose_language == "Deutsch":
        num1 = (input("Gebe die erste Nummer ein: "))
        while num1.isdigit() == False:
            num1 = (input("\033[31mDu hast keine erlaubte Nummer eingegeben. Probiere es nochmal:\033[0m "))

        num2 = (input("Gebe die zweite Nummer: "))
        while num2.isdigit() == False:
            num2 = (input("\033[31mDu hast keine erlaubte Nummer eingegeben. Probiere es nochmal:\033[0m "))
        
        num1 = float(num1)
        num2 = float(num2)

        if num1 > num2:
            result = num1/num2

        else:
            result = num2/num1

        print("------------------------------------------------------------------------")
        print(f"Das Resultat ist '{result}'.")


def power():
    if chose_language == "English":
        num1 = (input("Enter the base Number : "))
        while num1.isdigit() == False:
            num1 = (input("\033[31mYou didn't typed a valid Number. Try again:\033[0m "))

        num2 = (input("Enter the exponent Number: "))
        while num2.isdigit() == False:
            num2 = (input("\033[31mYou didn't typed a valid Number. Try again:\033[0m "))
        
        num1 = float(num1)
        num2 = float(num2)

        result = num1 ** num2

        print("------------------------------------------------------------------------")
        print(f"The result is '{result}'.")

    elif chose_language == "Deutsch":
        num1 = (input("Gebe die Basis Nummer ein: "))
        while num1.isdigit() == False:
            num1 = (input("\033[31mDu hast keine erlaubte Nummer eingegeben. Probiere es nochmal:\033[0m "))

        num2 = (input("Gebe die Exponent Nummer: "))
        while num2.isdigit() == False:
            num2 = (input("\033[31mDu hast keine erlaubte Nummer eingegeben. Probiere es nochmal:\033[0m "))
        
        num1 = float(num1)
        num2 = float(num2)

        result = num1 ** num2

        print("------------------------------------------------------------------------")
        print(f"Das Resultat ist '{result}'.")



while True:

    print("Supported Languages:")
    print("English")
    print("Deutsch")
    chose_language = input("Chose your language: ").title()


    if chose_language == "English":

        print("------------------------------------------------------------------------")
        print("Welcome to an Calculator coded with Python.")
        print("Just follow the steps.")
        print("At the moment you can only add 2 numbers.")
        print("At the moment, you can't go in the Minus-Area.")
        print("------------------------------------------------------------------------")


        while True:

            print("Chose, which Math you want to use: ")
            print("\033[34m+ for plus\033[0m")
            print("\033[36m- for minus\033[0m")
            print("\033[34m* for multiply\033[0m")
            print("\033[36m/ for divide\033[0m")
            print("\033[34m** for raising to power\033[0m")
            chose_math = input("Chose: ")
            print("------------------------------------------------------------------------")

            if chose_math == "+":
                plus()
            elif chose_math == "-":
                minus()
            elif chose_math == "*":
                multiply()
            elif chose_math == "/":
                divide()
            elif chose_math == "**":
                power()
            else:
                print("\033[31mDid you really chose a allowed Math? Try again:\033[0m ")
                print("------------------------------------------------------------------------")
                continue

                
            yn = input("Do you want to Calculate again? \033[1;92mYes\033[0m / \033[1;91mNo\033[0m: ").lower()

            if yn == "yes":
                print("------------------------------------------------------------------------")
                continue
                
            elif yn == "no":
                break
            else:
                print(f"You typed '{yn}'. The Programm doesn't know that.")
                yn = input("Do you want to try again? \033[1;92mYes\033[0m / \033[1;91mNo\033[0m: ").lower()

        if yn == "no":
            yn = input("Do you want to chose a other Language? \033[1;92mYes\033[0m / \033[1;91mNo\033[0m: ").lower()
            print("------------------------------------------------------------------------")

        if yn == "yes":
            continue
        elif yn == "no":
            input("Press Enter to close the Programm...")
            break

#-------------------------------------------------------------------------------------------------------------------------|
#   Deutsch                                                                                                               |
#-------------------------------------------------------------------------------------------------------------------------|

    elif chose_language == "Deutsch":

        print("------------------------------------------------------------------------")
        print("Willkommen zu einem Rechner, gecodet mit Python.")
        print("Floge einfach den Schritten.")
        print("Im Moment kann man nur 2 Zahlen zusammenrechnen.")
        print("Momentan, kann man nicht in den Minus-Bereich gehen.")
        print("------------------------------------------------------------------------")


        while True:

            print("Wähle aus welche Rechenart du möchtest: ")
            print("\033[34m+ für Plus\033[0m")
            print("\033[36m- für Minus\033[0m")
            print("\033[34m* für Mal\033[0m")
            print("\033[36m/ für Durch\033[0m")
            print("\033[34m** für Potenzieren\033[0m")
            chose_math = input("Wähle: ")
            print("------------------------------------------------------------------------")

            if chose_math == "+":
                plus()
            elif chose_math == "-":
                minus()
            elif chose_math == "*":
                multiply()
            elif chose_math == "/":
                divide()
            elif chose_math == "**":
                power()
            else:
                print("\033[31mHast du wirklich eines der erlaubten Zeichen verwendet? Probiere nochmal: \033[0m ")
                print("------------------------------------------------------------------------")
                continue

                
            yn = input("Möchtest du nochmal rechnen? \033[1;92mJa\033[0m / \033[1;91mNein\033[0m: ").lower()

            if yn == "ja":
                print("------------------------------------------------------------------------")
                continue
                
            elif yn == "nein":
                break
            else:
                print(f"Du hast geschrieben '{yn}'. Das Prgramm weis nicht was das ist.")
                yn = input("Möchtest du es nochmal probieren? \033[1;92mJa\033[0m / \033[1;91mNein\033[0m: ").lower()

        if yn == "nein":
            yn = input("Möchtest du eine andere Sprache wählen? \033[1;92mJa\033[0m / \033[1;91mNein\033[0m: ").lower()
            print("------------------------------------------------------------------------")
                
        if yn == "ja":
            continue
        elif yn == "nein":
            input("Drücke Enter um das Programm zu schliessen....")
            break

    else: # for the complet Prgramm 
        print("\033[31mAre you sure you picked a valid language? Try Again:\033[0m")
        print("------------------------------------------------------------------------")
