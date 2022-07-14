# Layout

from ast import While
from dis import dis
from hashlib import new
from imp import init_builtin
from mimetypes import init
from random import random
from mystery_bank import mystery_bank
import random

Play = ""
mys_num = 0
while Play == "" and mys_num <= len(mystery_bank):
    game_introduction = open("game_introduction.txt", "r")
    print(game_introduction.read())
    game_introduction.close()
    true_ans = mystery_bank[mys_num][0]

    def display(true_ans) :
        mystery_word = ""
        for letter in true_ans :
            if letter != " " :
                mystery_word = mystery_word + "_"
            else :
                mystery_word = mystery_word + " "
        return mystery_word

    # Checking 
    init_mys = display(true_ans)
    lives = 6
    while init_mys != true_ans and lives > 0 :
        print("Your word is : " + init_mys)
        print("Hint : " + mystery_bank[mys_num][1])
        print("Lives left : " + str(lives))
        new_mys = ""
        guess = input("Guess a letter or the whole word : ")
        for letter in true_ans :
            if letter.lower() == guess.lower() : 
                new_mys = new_mys + letter
            else :
                if letter == " " :
                    new_mys = new_mys + letter
                else :
                    new_mys = new_mys + "_"

        #Counting letters 
        def letter_count(word,letter) :
            i = 0
            for let in word :
                if let.lower() == letter.lower() :
                    i = i + 1
                else :
                    i = i + 0
            return i
        
        #Result
        if new_mys == display(true_ans) :
            print("Sike! 0 " + guess + " !")
            lives = lives - 1
        else :
            print("Correct guess! " + str(letter_count(true_ans,guess)) + " " + guess + " indeed!")
            lives = lives - 0

        end_phase_bar = open("end_phase_bar.txt", "r")
        print(end_phase_bar.read())
        end_phase_bar.close()
        
        #Overlap 
        def overlap(a,b) :
            decoy = ""
            for index in range (len(a)):
                if a[index] == "_" :
                    decoy = decoy + b[index]
                else :
                    decoy = decoy + a[index]
            a = decoy
            return a
        
        init_mys = overlap(init_mys,new_mys)

    #Play again
    if init_mys == true_ans :
        print("CONGRATS! THE WORD IS " + true_ans.upper() + " !")
    else :
        print("GAME OVER! THE WORD IS " + true_ans.upper() + " !")

    Play = input("Press Enter to play again : ")
    mys_num = mys_num + 1
print("oOo THE END oOo")

  

        



