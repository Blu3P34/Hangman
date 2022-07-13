a = "x_ _"
b = "__ a"

def overlap(a,b) :
    decoy = ""
    for index in range (len(a)):
        if a[index] == "_" :
            decoy = decoy + b[index]
        else :
            decoy = decoy + a[index]
    a = decoy
    return a

print(a)
