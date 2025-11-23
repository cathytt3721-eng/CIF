while question_right >= 20:
    hp=5

    from random import randint
    
    item= [
        ["Repel",["Repel remove monster from you."]],
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
        ["What is the most spoken language in the world?",["Mandarin","Chinese","chinese","mandarin"]],
        ["What is the chemical element with the symbol “O”?",["oxygen","Oxygen"]],
        ["Which planet is closest to the Sun?",["mercury","Mercury"]],
        ["What’s the main ingredient in chocolate?",["Cocoa bean","Cocoa Bean","cocoa Bean","cocoa bean"]],
    ]
    
    question = questionlist[randint(0,12)][0]
    answer = input(question)
    print(question)