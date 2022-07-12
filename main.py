print("Welcome to guessing game")
word = "Anakin"
print("This word has " + str(len(word)) + " letters \nYou have 5 chances")
guessing_word = None
guessing_limit = 0
guessing_count = 5
Hint = {
    "5" : "He is a StarWars character",
    "4" : "His lightsaber is blue",
    "3" : "He has prosthetic limbs",
    "2" : "He has the highest midi-chlorian count ever recored",
    "1" : "He is the chosen one"
}
while guessing_count > guessing_limit and guessing_word != word :
    print("Hint : " + Hint[str(guessing_count)])
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
