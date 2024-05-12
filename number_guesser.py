import random
def main():
    print("\n\t\t\tWELCOME TO THE NUMBER GUESSER !!!\n\n")
    print("Choose difficulty level:\n\n 1. Easy\n 2. Intermediate\n 3. Hard")
    print("\nChoose as 1, 2 or 3 respectively.")
    diff = int(input())

    match diff:
        case 1:
            easy()
        
        case 2:
            intermediate()
        
        case 3:
            hard()
        
        case _:
            print("Chosen difficulty is not available :(")


def easy():
    trials = 0
    print("\t\t\tYou chose Easy as your difficulty level.\n")
    print("Rules:\n \n 1. You must choose numbers greater than 30 to guess.\n 2. You shall have 10 trials to get the correct number. \n 3. If you exceed the trials, you'll lose the game.\n 4. You have no hints.")
    while True:
        n = input("\n\nUpto what number do you want to guess? ")

        if int(n) < 30:
            print("You need to choose numbers above 30 for this difficulty level.")
            continue
        if n.isdigit():
            random_number = random.randrange(0, int(n)+1)
            break
        
        else:
            print("Pick a number you dummy.")
            continue  

    
    while True:      
       
        user_choice = input("What's your guess? ")
        
        if user_choice.isdigit():
            if int(user_choice) > int(random_number):
                print("You guessed higher than the number.")
                trials += 1
                continue
            
            elif int(user_choice) < int(random_number):
                print("You guessed lower than the number.")
                trials += 1
                continue

            else:
                print("You got it. Congratulations :)")
                break
            
        else:
            print("Please enter a integer value.")
            trials += 1
            continue


    if trials <= 10:
        print("\n\nYou got it in", int(trials)+1, "trials. Congratulations, you won.")
        print("Thanks for playing.")
        
    else:
        print("\n\nYou got it in", int(trials)+1, "trials. You lost.")
        print("Thanks for playing.")

    
def intermediate():
    trials = 0
    print("\t\t\tYou chose Intermediate as your difficulty level.\n")
    print("Rules:\n \n 1. You must choose numbers greater than 50 to guess.\n 2. You shall have 7 trials to get the correct number. \n 3. If you exceed the trials, you'll lose the game.\n 4. You have 1 hint.")
    while True:
        n = input("\n\nUpto what number do you want to guess? ")

        if int(n) < 50:
            print("You need to choose numbers above 50 for this difficulty level.")
            continue
        if n.isdigit():
            random_number = random.randrange(0, int(n)+1)
            break
        
        else:
            print("Pick a number you dummy.")
            continue  

    i = 1
    while True:
        while i > 0:
            h = input("Do you want to use the only hint?(yes/no) ").lower()
            if h != "yes":
                print("Great\n\n")
                break
            else:
                if random_number % 2 == 0:
                        print("The required number is even.")
                else:
                        print("The required number is odd.")
                    
                i = i - 1
                   
        user_choice = input("What's your guess? ")
        
        if user_choice.isdigit():
            if int(user_choice) > int(random_number):
                print("You guessed higher than the number.")
                trials += 1
                continue
            
            elif int(user_choice) < int(random_number):
                print("You guessed lower than the number.")
                trials += 1
                continue

            
            else:
                print("You got it. Congratulations :)")
                break
            
        else:
            print("Please enter a integer value.")
            trials += 1
            continue


    if trials <= 7:
        print("\n\nYou got it in", int(trials)+1, "trials. Congratulations, you won.")
        print("Thanks for playing.")
        
    else:
        print("\n\nYou got it in", int(trials)+1, "trials. You lost.")
        print("Thanks for playing.")


def hard():
    trials = 0
    print("\t\t\tYou chose Hard as your difficulty level.\n")
    print("Rules:\n \n 1. You must choose numbers greater than 100 to guess.\n 2. You shall have 5 trials to get the correct number. \n 3. If you exceed the trials, you'll lose the game.\n 4. You have 2 hints.")
    while True:
        n = input("\n\nUpto what number do you want to guess? ")

        if int(n) < 100:
            print("You need to choose numbers above 100 for this difficulty level.")
            continue
        if n.isdigit():
            random_number = random.randrange(0, int(n)+1)
            break
        
        else:
            print("Pick a number you dummy.")
            continue  

    i = 1
    j = 1
    difference = 0
    while True:
        while i > 0:
            h = input("Do you want to use the first hint?(yes/no) ").lower()
            if h != "yes":
                print("Great\n\n")
                break
            else:
                if random_number % 2 == 0:
                        print("The required number is even.")
                else:
                        print("The required number is odd.")
                    
                i = i - 1
       
        
        while j > 0:
            h = input("Do you want to use the second hint?(yes/no) --> This hint reveals the answer.").lower()
            if h != "yes":
                print("Great\n\n")
                break
            else:
                reversed_num = 0
                while random_number != 0:

                    digit = random_number % 10
                    reversed_num = reversed_num * 10 + digit
                    random_number //= 10

                if reversed_num == random_number:
                    print("The number is palindrome.")
                else:
                    print("The number is non-palindrome.")
                
                j -= 1

        user_choice = input("What's your guess? ")
        
        if user_choice.isdigit():
            if int(user_choice) > int(random_number):
                print("You guessed higher than the number.")
                trials += 1
                continue
            
            elif int(user_choice) < int(random_number):
                print("You guessed lower than the number.")
                trials += 1
                continue

            else:
                print("You got it. Congratulations :)")
                break
            
        else:
            print("Please enter a integer value.")
            trials += 1
            continue


    if trials <= 5:
        print("\n\nYou got it in", int(trials)+1, "trials. Congratulations, you won.")
        print("Thanks for playing.")
        
    else:
        print("\n\nYou got it in", int(trials)+1, "trials. You lost.")
        print("Thanks for playing.")



main()