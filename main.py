# Layout

from ast import While
from dis import dis
from hashlib import new
from imp import init_builtin
from mimetypes import init
from random import random
from mystery_bank import mystery_bank
import random
from function import *

#Condition
Play = ""
mys_num = 0
ans = False
while Play == "" and mys_num <= len(mystery_bank) and ans == False:

    
    game_introduction = open("game_introduction.txt", "r")
    print(game_introduction.read())
    game_introduction.close()

    
    true_ans = mystery_bank[mys_num][0]

    #Print status
    init_mys = hide(true_ans)
    lives = 6
    while init_mys != true_ans and lives > 0 and ans == False:
        print("Your word is : " + init_mys)
        print("Hint : " + mystery_bank[mys_num][1])
        print("Lives left : " + str(lives))
        new_mys = ""
        guess = input("Guess a letter or the whole word : ")

        #Checking
        if len(guess) > 1 or len(guess) == 0 :
            if guess.lower() == true_ans.lower() :
                ans = True
                init_mys = guess
            else:
                print("Invalid input, please try again.")
                game_introduction = open("game_introduction.txt", "r")
                print(game_introduction.readline())
                game_introduction.close()
        else :
            for letter in true_ans :
                        if letter.lower() == guess.lower() : 
                            new_mys = new_mys + letter
                        else :
                            if letter == " " :
                                new_mys = new_mys + letter
                            else :
                                new_mys = new_mys + "_"
            
            #Result
            if new_mys == hide(true_ans) :
                print("Sike! 0 " + guess + " !")
                lives = lives - 1
            else :
                print("Correct guess! " + str(letter_count(true_ans,guess)) + " " + guess + " indeed!")
                lives = lives - 0

            game_introduction = open("game_introduction.txt", "r")
            print(game_introduction.readline())
            game_introduction.close()
            
            init_mys = overlap(init_mys,new_mys)

    #Play again
    game_introduction = open("game_introduction.txt", "r")
    print(game_introduction.readline())
    game_introduction.close()
    if init_mys.lower() == true_ans.lower() :
        print("CONGRATS! THE WORD IS " + true_ans.upper() + " !")
    else :
        print("GAME OVER! THE WORD IS " + true_ans.upper() + " !")

    Play = input("Press Enter to play again : ")
    mys_num = mys_num + 1
    ans = False
print("oOo THE END oOo")

  

        



