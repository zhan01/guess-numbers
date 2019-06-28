
number = 77
guess = input("\nGuess: ")
guess = int(guess)
counter = 1


while guess != number :
        if guess > number :
            print("Guess lower!")
        
        else:
            print("Guess higher!")
        print("-------------")

        guess = input("\nTry again: ")
        guess = int(guess)
        counter = counter + 1
        

print("\nYou won the game in " + str(counter) + " step(s) ! Congrats!")