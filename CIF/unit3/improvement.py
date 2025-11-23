    
from random import randint

# step 1: ask user decie the range
low=int(input("What do you want your lower number for the range be?"))
high=int(input("What do you want your higher number for the range be?"))

random_number= randint(low,high)  # both low bound and high bound are inclusive
trys=input("Guess what number in your range!")
if trys == random_number:
    ("Congratulation! You have won!")
   
else:
    print("Sorry not the right number!")



print("End Game")
  

