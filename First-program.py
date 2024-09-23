'''Asked gemini to give me a basic problem staement:

  Write a Python program that generates a random number between 1 and 100. The user should then guess the number. If the guess is too high or too low, the program should give a hint. The game should continue until the user guesses the correct number.
'''

import random
A = random.randint(1,100)

guesses = 0
while True:
    
    user_input = int(input("Guess The number: "))
    guesses+=1
    if user_input>A:
        print("the random number is smaller than", user_input)
    elif user_input<A:
        print("the random number is bigger than", user_input)
    else:
        print("Ding! Ding! Ding!, you guessed the number", A, "in",guesses,"guesses")
        play_again= input("Would you like to play again?(y/n)").lower()
        if play_again=="y":
            A = random.randint(1,100)
            guesses = 0
        else:    
         break
      
    