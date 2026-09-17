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
