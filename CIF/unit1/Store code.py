print("Welcome to the Fruit Store")

print("Here is the list of fruit you can buy in my store.")

my_list = ["1.apple $1.00 each", "2.banana $1.00 each", "3.pear $2.00 each", "4.strawberry $5.00 each box", "5.blueberry $4.00 each box", "6.orange $1.50 each", "7.pineapple $6.00 each"]
print(my_list[0]) #output apple
print(my_list[1]) #output banana
print(my_list[2]) #output pear
print(my_list[3]) #output strawberry
print(my_list[4]) #output blueberryj
print(my_list[5]) #output orange
print(my_list[6]) #output pineapple

buy_again="yes"

while buy_again == "yes":
    what_fruit=input(" What do you want to buy?")
    how_many=input("How many do you want to buy?")   

    coupon=str(input("Do you have a coupon?(yes/no)"))
    if coupon == "yes":
        print("You got 10% off")
    else:
        print("Sorry you don't get 10% off")

    total_price= what_fruit + how_many

    print("The total price is $")
        
    buy_again=input("Do you want to buy more? (yes/no)")






    
    