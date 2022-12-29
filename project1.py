from time import sleep

question1 = question2 = question3 = question4 = " "

print("=" * 30)
print("\033[33mWELCOME TO MY QUIZ GAME...\033[m")
print("=" * 30)
answer = input("Would you like to play? ").upper()[0]
if answer == "N":
    print("Ok, see you next time...")
    quit()
sleep(1)
print("Okay, let's play!")
sleep(1)
question1 = input("What is the best TV series ever? ").upper()
while question1 != "FRIENDS":
    print("\033[31mTry again !!\033[m")
    question1 = input("What is the best TV series ever? ").upper()
cont = input("\033[32mGOOD!!! Would you like to continue? \033[m").upper()[0]
if cont != "Y":
    print("Ok, see you next time...")
else:
    question2 = input("What is my favorite food? ").upper()
    while question2 != "SUSHI":
        print("\033[31mTry again !!\033[m")
        question2 = input("What is my favorite food? ").upper()
    cont = input("\033[32mGOOD!!! Would you like to continue? \033[m").upper()[0]
    if cont != "Y":
        print("Ok, see you next time...")
    else:
        question3 = input("What was the first programming language I learned? ").upper()
        while question3 != "PASCAL":
            print("\033[31m Try again !!\033[m")
            question3 = input(
                "What was the first programming language I learned? "
            ).upper()
        cont = input(
            "\033[32mGOOD!!! Would you like to continue? \033[m"
        ).upper()[0]
        if cont != "Y":
            print("Ok, see you next time...")
        else:
            question4 = input(
                "What was the second programming language I learned? "
            ).upper()
            while question4 != "PYTHON":
                print("\033[31m Try again !! \033[m")
                question4 = input(
                    "What was the second programming language I learned? "
                ).upper()
            print("\033[32mGOOD!! \n  See you next time .. \033[m! ! ")
