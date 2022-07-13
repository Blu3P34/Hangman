# Layout

from dis import dis
from hashlib import new
from imp import init_builtin
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

# Checking function 
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

    #Counting letters fucntion
    def letter_count(word,letter) :
        i = 0
        for let in word :
            if let.lower() == letter.lower() :
                i = i + 1
            else :
                i = i + 0
        return i

    if new_mys == display(true_ans) :
        print("Sike! 0 " + guess + " !")
    else :
        print("Correct guess! " + str(letter_count(true_ans,guess)) + " " + guess + " indeed!")

    end_phase_bar = open("end_phase_bar.txt", "r")
    print(end_phase_bar.read())
    end_phase_bar.close()
    
    #Overlap function
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

  

        



