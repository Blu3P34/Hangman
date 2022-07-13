def hangman(guess):
    answer = "Apple"
    display_ans = ""
    for letter in answer :
        if letter.lower() == guess.lower() :
            display_ans = display_ans + letter
        else :
            display_ans = display_ans + "_"
    print(display_ans)
print(hangman("L"))

