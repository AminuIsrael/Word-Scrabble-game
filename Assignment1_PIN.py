"""
Created on Sun Apr  7 18:48:27 2019

@author: Israel
"""

import random
data = open("words.txt", 'r')
#convert the dictionary .txt to lists
dict_to_list = [line.split(',') for line in data.readlines()]


#Converting the random list to string
value = random.choice(dict_to_list)
to_string = str(''.join(value)).rstrip("\n")
#print(to_string)


#Hint for the game...Because its too hard
hint = to_string[0:3]

#To scramble the word using the shuffle function
scr_val = list(to_string)   
random.shuffle(scr_val)
scr_word = "".join(scr_val)

#Game_play :)
print("-------------------------------------------------------------------------------")
print("                       Welcome to the Word Scrabble game \n")
print("         You are to re-arrange a scrabbled word collected from a dictionary\n")
print("                        You only have 3 lives. Good Luck :)")
print("-------------------------------------------------------------------------------")
print(f"Guess the word:{scr_word}\n")

print(f"Hint:{hint}...\n")

i = 0 

while i < 3:
    user_val = input("Enter Word here: ")
    if to_string == user_val:
        print("Correct!!!")
        break
    else:
        print("Not correct\n")
    i = i+1

if user_val == to_string:
    print("")
else:
    print(f"The correct word is {to_string}")

  














