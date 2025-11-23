print("Welcome to the game")

#ask the player if want to play
answer =input("Do you want to play!")

if answer == "yes":
    print("Let's play")

else:
    print("End Game!!!!")


from random import randint

# step 1: ask user decie the range
low=int(input("What do you want your lower number for the range be?"))
high=int(input("What do you want your higher number for the range be?"))

random_number= randint(low,high)  # both low bound and high bound are inclusive

# set up the max try
max_trials=3

print("You will get {max_trials} trys")
while max_trials >= 0:
    
    trys=int(input("Guess the number between your range!"))
    
    if trys == random_number: 
        ("Congratulation! You have won!")
        break
    else:
        if trys >=random_number:
            print("Sorry not the right number! Try again.")
            print("It's too big")
            print("You have {max_trials} left")
        else:
            print("Sorry not the right number! Try again.")
            print("It's too small")
            print("You have {max_trials} left")
    max_trials = max_trials -1 

print("End Game")