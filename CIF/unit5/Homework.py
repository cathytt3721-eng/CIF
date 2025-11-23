print("--------------------------------------")
print("\t How to Play")
print("--------------------------------------")
   
print("At the start of the you will get 3 lives" \
    "\nIn the game you need to answer 20 question right to win" \
    "\nWhen you answer the question right, you will get a item that you can used" \
    "\nYou get three item spaces to store item that you can use later " \
    "To use a item from you inventory, you need to type it out." \
    "\nBut if you answer a question wrong, you lose one live." \
    "\nThere while may be mimic in your chest, attack dealing (1-2 hearts). You get 5 sec before it attack" \
    "To get rid of it you need to use the item (repelent) to get rid of it")
print("--------------------------------------")

def rule():
    print(rule)
    return

question_right=0

while question_right >= 20:
    
    import sys

    from random import randint
    
    item= [
        ["Repelent",["Repel remove monster from you."]],
        ["Medkit",["Heal one heart "]],
        ["Mimic"["It will deal(1-2 hearts)"]]
        ["Nothing"],
    ]
    chest= randint(item)
    
    questionlist = [
        ["What is the fastest land animal?",["Cheetah","cheetah"]],
        ["What is the fastest land animal?",["Jupiter","jupiter"]],
        ["What is the largest organ on the human body?",["Skin","skin"]],
        ["Where is the Giant Panda found?",["China","china"]],
        ["What country is responsible for creating the Olympic Games?",["Greece","greece"]],
        ["What shape is the stop sign?",["octagon","Octagon"]],
        ["What is the world’s smallest continent?",["australia","Australia"]],
        ["What is the largest mammal in the world?",["Blue whale","blue whale","Blue Whale","blue Whale"]],
        ["Which planet is known as the Red Planet?",["Mars","mars"]],
        ["What is the chemical element with the symbol “O”?",["oxygen","Oxygen"]],
        ["Which planet is closest to the Sun?",["mercury","Mercury"]],
        ["What’s the main ingredient in chocolate?",["Cocoa bean","Cocoa Bean","cocoa Bean","cocoa bean"]],
        
    ]
    
    question = questionlist[randint(0,12)][0]
    answer = input(question)
    print(question)
    
    if(answer in questionlist[randint(0,12)][1]):
        question_right=question_right+1
        treasure=randint(chest)
    else:
        print("You are wrong and loss 1 live")
        hp=hp-1

    if chest =='Mimic':
        print("You've got a mimic")

    elif not chest =='Mimic':
        print("You've got a ",chest)
        store=input("Do you want to store it.")

            
    hp=5
    if hp == 0:
        print("You lost")
        sys.exit()
    else:
        print("You have",hp)
        
        if store =='Medkit':
            heal=input("Do you want to heal one heart with your Medkit")
            if heal =='Yes':
                hp+1
                print("You have",hp)
        else:
            print("You have no Medkits")