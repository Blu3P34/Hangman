# Layout

from dis import dis
from hashlib import new
from mimetypes import init


game_introduction = open("game_introduction.txt", "r")
print(game_introduction.read())
game_introduction.close()

true_ans = "Anakin Skywalker"

def display(true_ans) :
    mystery_word = ""
    for letter in true_ans :
        if letter != " " :
            mystery_word = mystery_word + "_"
        else :
            mystery_word = mystery_word + " "
    return mystery_word

# Game function 
init_mys = display(true_ans)

while init_mys != true_ans :
    print("Your word is : " + init_mys)
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

        



