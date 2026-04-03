import random
autoNum = random.randint(1, 20)
try:
    guess = int(input("Enter your guess: "))
   
    if guess < autoNum:
        print("Too Low")
    elif guess > autoNum:
        print("Too High")
    else:
        print("Correct")
except ValueError:
    print("Please enter a valid number!")