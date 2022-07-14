#Hide true answer
def hide(a) :
    b = ""
    for letter in a :
        if letter != " " :
            b = b + "_"
        else :
            b = b + " "
    return b

#Counting letter in a word
def letter_count(word,letter) :
                i = 0
                for let in word :
                    if let.lower() == letter.lower() :
                        i = i + 1
                    else :
                        i = i + 0
                return i

#Overwrite new hidden answer
def overlap(a,b) :
                decoy = ""
                for index in range (len(a)):
                    if a[index] == "_" :
                        decoy = decoy + b[index]
                    else :
                        decoy = decoy + a[index]
                a = decoy
                return a
            