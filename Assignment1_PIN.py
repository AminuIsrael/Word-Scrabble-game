"""
Created on Sun Apr  14 22:18:27 2019

@author: Israel
"""
print("-------------------------------------------------------------------------------")
print("                       Welcome to the Word Scrabble game \n")
print("         You are to re-arrange a scrabbled word collected from a dictionary\n")
print("                        You only have 3 lives. Good Luck :)")
print("-------------------------------------------------------------------------------")
i = 3
score = 0 

while i > 0:
    data = open("words.txt", 'r')
    dict_to_list = [line.split(',') for line in data.readlines()]


    import random
    value = random.choice(dict_to_list)
    to_string = ''.join(value).rstrip("\n").lower()
    #print(to_string)

    hint = to_string[0:3]

    scr_val = list(to_string)   
    random.shuffle(scr_val)
    scr_word = "".join(scr_val)
    print("=====================")
    print(f"Guess the word:\n{scr_word}\n")
    print(f"Hint:{hint}...")
    print("=====================")

    user_val = (input("Enter Word here: \n")).lower()
    if to_string == user_val:
        print("Correct!!!")
        score += 10
        print(f"You have {score} points\n")
    else:
        print("Wrong!!!")
        print(f"The correct word is {to_string}")
        i = i-1
        print(f"You have {i} lives left\n")
        

if score >= 10:
    print("Game Over")
    print(f"You have a total of {score} points, good job.")
else:
    print("Game Over")
    print("You have 0 points")

  














