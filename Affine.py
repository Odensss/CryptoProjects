# This code implements affine chiffre
# const
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def enc(a, b):
    output = ""
    with open("encode.txt", "r") as f:
        text = f.read()
        for c in text:
            if c.upper() in alphabet:
                output += alphabet[(alphabet.index(c.upper()) * a + b) % 26]
            elif c == " ":
                output += " "
        print(output)
        output = ""

enc(1,0)
