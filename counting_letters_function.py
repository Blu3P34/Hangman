def letter_count(word,letter) :
    i = 0
    for let in word :
        if let == letter :
            i = i + 1
        else :
            i = i + 0
    return i
print(letter_count("abaca","a"))


