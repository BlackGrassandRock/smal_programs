import random

for ist in range (100):

    #create random letter
    rand_f = chr(random.randint(ord('a'), ord('z')))
    mail = rand_f


    #Markov chain
    alphabet = {
        "a" : ("n", "t", "l", "r", "s"),
        "b" : ("e", "u", "a", "i"),
        "c" : ("o", "e", "h", "i", "t"),
        "d" : ("e", "a", "i", "u"),
        "e" : ("r", "n", "s", "d", "a"),
        "f" : ("e", "a", "t", "g"),
        "g" : ("e", "h", "o", "l"),
        "h" : ("e", "a", "i", "o"),
        "i" : ("n", "t", "o", "c"),
        "j" : ("a", "e", "i", "o", "u"),
        "k" : ("i", "e", "w", "y"),
        "l" : ("e", "i", "l", "o"),
        "m" : ("e", "a", "i", "o"),
        "n" : ("d", "t", "e", "c"),
        "o" : ("n", "r", "f", "u", "m"),
        "p" : ("a", "i", "o", "w"), 
        "q" : "u",
        "r" : ("e", "i", "o", "a"),
        "s" : ("t", "i", "e", "a"),
        "t" : ("h", "i", "e", "o"), 
        "u" : ("r", "s", "t", "n"),
        "v" : ("e", "a", "i", "o"),
        "w" : ("a", "i", "h", "o"),
        "x" : ("a", "c", "l", "p"),
        "y" : ("a", "f", "o", "z"),
        "z" : ("a", "l", "h", "e")}

    for i in range(8):

        #Learns the length of the chain
        ln_list = len(alphabet[mail[-1]])

        #Choosing an element from the chain
        rand_folow = random.randint(0, ln_list - 1)

        #Add the next letter
        mail += alphabet[mail[-1]][rand_folow]

    mail += "."

    #Generalize the numbers for the mail
    for i in range(2):
        mail += str(random.randint(1, 9))

    mail += "."
    for i in range(3):
        rand_f = chr(random.randint(ord('a'), ord('z')))
        mail += rand_f

    mail += "@gmail.com"

    print(ist + 1, ") ", mail)

