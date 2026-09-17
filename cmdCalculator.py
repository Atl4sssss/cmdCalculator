def plus():

    if chose_language == "English":
        num1 = (input("\033[33mEnter the first Number:\033[0m "))
        while num1.isdigit() == False:
            num1 = (input("\033[31mYou didn't typed a valid Number! \033[33mTry again:\033[0m "))

        num2 = (input("\033[33mEnter the second Number:\033[0m "))
        while num2.isdigit() == False:
            num2 = (input("\033[31mYou didn't typed a valid Number! \033[33mTry again:\033[0m "))
        
        num1 = float(num1)
        num2 = float(num2)

        result = num1 + num2

        print("------------------------------------------------------------------------")
        print(f"The result is \033[38;5;46m'{result}'\033[0m'.")

    elif chose_language == "Deutsch":
        num1 = (input("\033[33mGebe die erste Nummer ein:\033[0m "))
        while num1.isdigit() == False:
            num1 = (input("\033[31mDu hast keine erlaubte Nummer eingegeben! \033[33mProbiere es nochmal:\033[0m "))

        num2 = (input("\033[33mGebe die zweite Nummer ein:\033[0m "))
        while num2.isdigit() == False:
            num2 = (input("\033[31mDu hast keine erlaubte Nummer eingegeben! \033[33mProbiere es nochmal:\033[0m "))
        
        num1 = float(num1)
        num2 = float(num2)

        result = num1 + num2

        print("------------------------------------------------------------------------")
        print(f"Das Resultat ist \033[38;5;46m'{result}'\033[0m.")

    elif chose_language == "Français":
        num1 = (input("\033[33mSaisis le premier numéro:\033[0m "))
        while num1.isdigit() == False:
            num1 = (input("\033[31mTu n'as pas saisi de numéro valide! \033[33mRéessaie:\033[0m "))

        num2 = (input("\033[33mSaisis le deuxième numéro:\033[0m "))
        while num2.isdigit() == False:
            num2 = (input("\033[31mTu n'as pas saisi de numéro valide! \033[33mRéessaie:\033[0m "))
        
        num1 = float(num1)
        num2 = float(num2)

        result = num1 + num2

        print("------------------------------------------------------------------------")
        print(f"Le résultat est \033[38;5;46m'{result}'\033[0m.")


def minus():

    if chose_language == "English":
        num1 = (input("\033[33mEnter the first Number:\033[0m "))
        while num1.isdigit() == False:
            num1 = (input("\033[31mYou didn't typed a valid Number! \033[33mTry again:\033[0m "))

        num2 = (input("\033[33mEnter the second Number:\033[0m "))
        while num2.isdigit() == False:
            num2 = (input("\033[31mYou didn't typed a valid Number! \033[33mTry again:\033[0m "))
        
        num1 = float(num1)
        num2 = float(num2)

        result = num1 - num2

        print("------------------------------------------------------------------------")
        print(f"The result is \033[38;5;46m'{result}'\033[0m.")

    elif chose_language == "Deutsch":
        num1 = (input("\033[33mGebe die erste Nummer ein:\033[0m "))
        while num1.isdigit() == False:
            num1 = (input("\033[31mDu hast keine erlaubte Nummer eingegeben! \033[33mProbiere es nochmal:\033[0m "))

        num2 = (input("\033[33mGebe die zweite Nummer ein:\033[0m "))
        while num2.isdigit() == False:
            num2 = (input("\033[31mDu hast keine erlaubte Nummer eingegeben! \033[33mProbiere es nochmal:\033[0m "))
        
        num1 = float(num1)
        num2 = float(num2)

        result = num1 - num2

        print("------------------------------------------------------------------------")
        print(f"Das Resultat ist \033[38;5;46m'{result}'\033[0m.")

    elif chose_language == "Français":
        num1 = (input("\033[33mSaisis le premier numéro:\033[0m "))
        while num1.isdigit() == False:
            num1 = (input("\033[31mTu n'as pas saisi de numéro valide! \033[33mRéessaie:\033[0m "))

        num2 = (input("\033[33mSaisis le deuxième numéro:\033[0m "))
        while num2.isdigit() == False:
            num2 = (input("\033[31mTu n'as pas saisi de numéro valide! \033[33mRéessaie:\033[0m "))
        
        num1 = float(num1)
        num2 = float(num2)

        result = num1 - num2

        print("------------------------------------------------------------------------")
        print(f"Le résultat est \033[38;5;46m'{result}'\033[0m.")


def multiply():

    if chose_language == "English":
        num1 = (input("\033[33mEnter the first Number:\033[0m "))
        while num1.isdigit() == False:
            num1 = (input("\033[31mYou didn't typed a valid Number! \033[33mTry again:\033[0m "))

        num2 = (input("\033[33mEnter the second Number:\033[0m "))
        while num2.isdigit() == False:
            num2 = (input("\033[31mYou didn't typed a valid Number! \033[33mTry again:\033[0m "))
        
        num1 = float(num1)
        num2 = float(num2)

        result = num1 * num2

        print("------------------------------------------------------------------------")
        print(f"The result is \033[38;5;46m'{result}'\033[0m.")

    elif chose_language == "Deutsch":
        num1 = (input("\033[33mGebe die erste Nummer ein:\033[0m "))
        while num1.isdigit() == False:
            num1 = (input("\033[31mDu hast keine erlaubte Nummer eingegeben! \033[33mProbiere es nochmal:\033[0m "))

        num2 = (input("\033[33mGebe die zweite Nummer ein:\033[0m "))
        while num2.isdigit() == False:
            num2 = (input("\033[31mDu hast keine erlaubte Nummer eingegeben! \033[33mProbiere es nochmal:\033[0m "))
        
        num1 = float(num1)
        num2 = float(num2)

        result = num1 * num2

        print("------------------------------------------------------------------------")
        print(f"Das Resultat ist \033[38;5;46m'{result}'\033[0m'.")

    elif chose_language == "Français":
        num1 = (input("\033[33mSaisis le premier numéro:\033[0m "))
        while num1.isdigit() == False:
            num1 = (input("\033[31mTu n'as pas saisi de numéro valide! \033[33mRéessaie:\033[0m "))

        num2 = (input("\033[33mSaisis le deuxième numéro:\033[0m "))
        while num2.isdigit() == False:
            num2 = (input("\033[31mTu n'as pas saisi de numéro valide! \033[33mRéessaie:\033[0m "))
        
        num1 = float(num1)
        num2 = float(num2)

        result = num1 * num2

        print("------------------------------------------------------------------------")
        print(f"Le résultat est \033[38;5;46m'{result}'\033[0m.")


def divide():

    if chose_language == "English":
        num1 = (input("\033[33mEnter the first Number:\033[0m "))
        while num1.isdigit() == False:
            num1 = (input("\033[31mYou didn't typed a valid Number! \033[33mTry again:\033[0m "))

        num2 = (input("\033[33mEnter the second Number:\033[0m "))
        while num2.isdigit() == False:
            num2 = (input("\033[31mYou didn't typed a valid Number! \033[33mTry again:\033[0m "))
        
        num1 = float(num1)
        num2 = float(num2)

        result = num1 / num2 

        print("------------------------------------------------------------------------")
        print(f"The result is \033[38;5;46m'{result}'\033[0m.")

    elif chose_language == "Deutsch":
        num1 = (input("\033[33mGebe die erste Nummer ein:\033[0m "))
        while num1.isdigit() == False:
            num1 = (input("\033[31mDu hast keine erlaubte Nummer eingegeben! \033[33mProbiere es nochmal:\033[0m "))

        num2 = (input("\033[33mGebe die zweite Nummer ein:\033[0m "))
        while num2.isdigit() == False:
            num2 = (input("\033[31mDu hast keine erlaubte Nummer eingegeben! \033[33mProbiere es nochmal:\033[0m "))
        
        num1 = float(num1)
        num2 = float(num2)

        result = num1 / num2 

        print("------------------------------------------------------------------------")
        print(f"Das Resultat ist '{result}'.")

    elif chose_language == "Français":
        num1 = (input("\033[33mSaisis le premier numéro:\033[0m "))
        while num1.isdigit() == False:
            num1 = (input("\033[31mTu n'as pas saisi de numéro valide! \033[33mRéessaie:\033[0m "))

        num2 = (input("\033[33mSaisis le deuxième numéro:\033[0m "))
        while num2.isdigit() == False:
            num2 = (input("\033[31mTu n'as pas saisi de numéro valide! \033[33mRéessaie:\033[0m "))
        
        num1 = float(num1)
        num2 = float(num2)

        result = num1 / num2

        print("------------------------------------------------------------------------")
        print(f"Le résultat est \033[38;5;46m'{result}'\033[0m.")


def power():

    if chose_language == "English":
        num1 = (input("\033[33mEnter the base Number:\033[0m "))
        while num1.isdigit() == False:
            num1 = (input("\033[31mYou didn't typed a valid Number. \033[33mTry again:\033[0m "))

        num2 = (input("\033[33mEnter the exponent Number:\033[0m "))
        while num2.isdigit() == False:
            num2 = (input("\033[31mYou didn't typed a valid Number. \033[33mTry again:\033[0m "))
        
        num1 = float(num1)
        num2 = float(num2)

        result = num1 ** num2

        print("------------------------------------------------------------------------")
        print(f"The result is \033[38;5;46m'{result}'\033[0m.")

    elif chose_language == "Deutsch":
        num1 = (input("\033[33mGebe die Basis Nummer ein:\033[0m "))
        while num1.isdigit() == False:
            num1 = (input("\033[31mDu hast keine erlaubte Nummer eingegeben. \033[33mProbiere es nochmal:\033[0m "))

        num2 = (input("\033[33mGebe die Exponent Nummer:\033[0m "))
        while num2.isdigit() == False:
            num2 = (input("\033[31mDu hast keine erlaubte Nummer eingegeben. \033[33mProbiere es nochmal:\033[0m "))
        
        num1 = float(num1)
        num2 = float(num2)

        result = num1 ** num2

        print("------------------------------------------------------------------------")
        print(f"Das Resultat ist \033[38;5;46m'{result}'\033[0m.")

    elif chose_language == "Français":
        num1 = (input("\033[33mSaisissez le numéro de base:\033[0m "))
        while num1.isdigit() == False:
            num1 = (input("\033[31mTu n'as pas saisi de numéro valide! \033[33mRéessaie:\033[0m "))

        num2 = (input("\033[33mIndiquez le numéro de l'exposant \033[0m "))
        while num2.isdigit() == False:
            num2 = (input("\033[31mTu n'as pas saisi de numéro valide! \033[33mRéessaie:\033[0m "))
        
        num1 = float(num1)
        num2 = float(num2)

        result = num1 + num2

        print("------------------------------------------------------------------------")
        print(f"Le résultat est \033[38;5;46m'{result}'\033[0m.")



while True:

    print("\033[1mSupported Languages: / Unterstütze Sprachen: / Langues prises en charge:\033[0m")
    print("\033[38;5;27mEnglish\033[0m")
    print("\033[36mDeutsch\033[0m")
    print("\033[38;5;27mFrançais\033[0m")
    chose_language = input("\033[33mChose your language: / Wähle eine Sprache: / Choisissez une langue:\033[0m ").title()


#-------------------------------------------------------------------------------------------------------------------------|
#   English                                                                                                               |
#-------------------------------------------------------------------------------------------------------------------------|


    if chose_language == "English":

        print("------------------------------------------------------------------------")
        print("Welcome to an Calculator coded with Python.")
        print("Just follow the steps.")
        print("You can only add 2 numbers. \033[1;95mI will not add more!\033[0m")
        print("------------------------------------------------------------------------")


        while True:

            print("\033[1mChose, which Math you want to use:\033[0m")
            print("\033[38;5;27m+ for plus\033[0m")
            print("\033[36m- for minus\033[0m")
            print("\033[38;5;27m* for multiply\033[0m")
            print("\033[36m/ for divide\033[0m")
            print("\033[38;5;27m** for raising to power\033[0m")
            chose_math = input("\033[33mChose:\033[0m ")
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
                print(f"\033[31mYou typed \033[1m'{chose_math}'.\033[0m \033[31mThat isn't allowed Math! \033[33mTry again:\033[0m")
                print("------------------------------------------------------------------------")
                continue

                
            yn = input("\033[33mDo you want to Calculate again?\033[0m \033[1;92mYes\033[0m / \033[1;91mNo\033[0m: ").lower()
            print("------------------------------------------------------------------------")

            if yn == "yes":
                continue
                
            elif yn == "no":
                break
            else:
                print(f"\033[31mYou typed \033[1m'{yn}'\033[0m. \033[31mThat's not a allowed answer!\033[0m")
                yn = input("\033[33mDo you want to Calculate again?\033[0m \033[1;92mYes\033[0m / \033[1;91mNo\033[0m: ").lower()
                print("------------------------------------------------------------------------")

                if yn == "yes":
                    continue
                elif yn == "no":
                    break
                else:
                    break

        if yn == "no":
            yn = input("\033[33mDo you want to chose a other Language?\033[0m \033[1;92mYes\033[0m / \033[1;91mNo\033[0m: ").lower()
            print("------------------------------------------------------------------------")

        if yn == "yes":
            continue
        elif yn == "no":
            input("\033[33mPress Enter to close the Programm...\033[0m")
            break
        else:
            print(f"\033[31mYou typed \033[1m'{yn}'\033[0m. \033[31mThat's not a allowed answer! The Programm will close:\033[0m")
            input("\033[33mPress Enter to close the Programm...\033[0m")
            break

#-------------------------------------------------------------------------------------------------------------------------|
#   Deutsch                                                                                                               |
#-------------------------------------------------------------------------------------------------------------------------|

    if chose_language == "Deutsch":

        print("------------------------------------------------------------------------")
        print("Wilkommen zu einem Mathe-Rechner, gecodet mit Python.")
        print("Folge einfach den Schritten.")
        print("Du kannst nur 2 Nummern hinzufügen. \033[1;95mIch werde nicht mehr hinzufügen!\033[0m")
        print("------------------------------------------------------------------------")


        while True:

            print("\033[1mWähle eine Rechenart:\033[0m")
            print("\033[38;5;27m+ für Plus\033[0m")
            print("\033[36m- für Minus\033[0m")
            print("\033[38;5;27m* für Mal\033[0m")
            print("\033[36m/ für Durch\033[0m")
            print("\033[38;5;27m** für hoch-rechnen\033[0m")
            chose_math = input("\033[33mWähle:\033[0m ")
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
                print(f"\033[31mDu hast geschrieben \033[1m'{chose_math}'.\033[0m \033[31mDas ist keine unterstützed Rechenart! \033[33mProbier nochmal:\033[0m")
                print("------------------------------------------------------------------------")
                continue

                
            yn = input("\033[33mMöchtest du nochmal Rechnen?\033[0m \033[1;92mJa\033[0m / \033[1;91mNein\033[0m: ").lower()
            print("------------------------------------------------------------------------")

            if yn == "ja":
                continue
                
            elif yn == "nein":
                break
            else:
                print(f"\033[31mDu hast geschrieben \033[1m'{yn}'\033[0m. \033[31mDas ist keine erlaubte Antwort!\033[0m")
                yn = input("\033[33mMöchtest du nochmal Rechnen?\033[0m \033[1;92mJa\033[0m / \033[1;91mNein\033[0m: ").lower()
                print("------------------------------------------------------------------------")

                if yn == "ja":
                    continue
                elif yn == "nein":
                    break
                else:
                    break

        if yn == "nein":
            yn = input("\033[33mMöchtest du eine andere Sprache wählen?\033[0m \033[1;92mJa\033[0m / \033[1;91mNein\033[0m: ").lower()
            print("------------------------------------------------------------------------")

        if yn == "ja":
            continue
        elif yn == "nein":
            input("\033[33mDrücke Enter um das Programm zu schliessen...\033[0m")
            break
        else:
            print(f"\033[31mDu hast geschrieben \033[1m'{yn}'\033[0m. \033[31mDas ist keine erlaubte Antwort! Das Programm wird schliessen:\033[0m")
            input("\033[33mDrücke Enter um das Programm zu schliessen...\033[0m")
            break

#-------------------------------------------------------------------------------------------------------------------------|
#   Français                                                                                                                   |
#-------------------------------------------------------------------------------------------------------------------------|

    if chose_language == "Français":

        print("------------------------------------------------------------------------")
        print("Bienvenue sur cette calculatrice mathématique, programmée en Python.")
        print("Il suffit de suivre les étapes.")
        print("Tu ne peux ajouter que 2 numéros. \033[1;95mJe n'ajouterai rien d'autre!\033[0m")
        print("------------------------------------------------------------------------")


        while True:

            print("\033[1mChoisissez un mode de calcul:\033[0m")
            print("\033[38;5;27m+ pour Plus\033[0m")
            print("\033[36m- pour moins\033[0m")
            print("\033[38;5;27m* pour fois\033[0m")
            print("\033[36m/ pour divisé par\033[0m")
            print("\033[38;5;27m** pour calculer une proportion\033[0m")
            chose_math = input("\033[33mChoisis:\033[0m ")
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
                print(f"\033[31mTu as écrit \033[1m'{chose_math}'.\033[0m \033[31mCe type de calcul n'est pas pris en charge! \033[33mRéessaie:\033[0m")
                print("------------------------------------------------------------------------")
                continue

                
            yn = input("\033[33mTu veux refaire un peu de maths?\033[0m \033[1;92mOui\033[0m / \033[1;91mNon\033[0m: ").lower()
            print("------------------------------------------------------------------------")

            if yn == "oui":
                continue
                
            elif yn == "non":
                break
            else:
                print(f"\033[31mTu as écrit \033[1m'{chose_math}'.\033[0m \033[31mCe type de calcul n'est pas pris en charge!\033[0m")
                yn = input("\033[33mTu veux refaire un peu de maths?\033[0m \033[1;92mOui\033[0m / \033[1;91mNon\033[0m: ").lower()
                print("------------------------------------------------------------------------")

                if yn == "oui":
                    continue
                elif yn == "non":
                    break
                else:
                    break

        if yn == "non":
            yn = input("\033[33mSouhaites-tu choisir une autre langue?\033[0m \033[1;92mOui\033[0m / \033[1;91mNon\033[0m: ").lower()
            print("------------------------------------------------------------------------")

        if yn == "oui":
            continue
        elif yn == "non":
            input("\033[33mAppuie sur Entrée pour fermer le programme...\033[0m")
            break
        else:
            print(f"\033[31mTu as écrit \033[1m'{yn}'\033[0m. \033[31mCe n'est pas une réponse valable! Le programme va se fermer:\033[0m")
            input("\033[33mAppuie sur Entrée pour fermer le programme...\033[0m")
            break


#-------------------------------------------------------------------------------------------------------------------------|
#   End                                                                                                                   |
#-------------------------------------------------------------------------------------------------------------------------|
    else: 
        print(f"\033[31mYou typed \033[1m'{chose_language}'.\033[0m \033[31mThat isn't a supported Language! Try again:\033[0m")
        print("------------------------------------------------------------------------")
