print("Welcome to the game")

answer =input("Do you want to play!")

if answer == "yes":
    print("Let's play")

else:
    print("End Game!!!!")


from random import randint

random_number= randint(0, 100)
number=2

while number >= 0:
    trys=int(input("Guess what number from 1-100! You get" ,number ))


    if trys == random_number:
        ("Congratulation! You have won!")
    else:
        print("Sorry not the right number! Try again.")
        print("You have",number ("left"))
    
    number = number -1 

