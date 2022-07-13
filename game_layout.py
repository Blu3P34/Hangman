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
    print("Your word is : \n" + mystery_word)

display(true_ans)
