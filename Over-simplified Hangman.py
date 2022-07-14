print("Welcome to over-simplified Hangman")
word = "Anakin"
print("You have 5 chances")
guessing_word = None
guessing_limit = 0
guessing_count = 6
Hint = "StarWars character."

while guessing_count > guessing_limit and guessing_word != word :
    print("Hint : " + Hint)
    guessing_word = input("guess : ")
    if guessing_word == word :
        print("Congrats, the word is indeed " + word)
    else :
        guessing_count = guessing_count - 1
        print("Wrong !\nGuessing turn left : " + str(guessing_count))
        if guessing_count == guessing_limit :
            print("You lose dumbass !")
        else :
            print("Try again !")
