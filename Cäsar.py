#This code is an implementation of Caesar Chiffre

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def dec():
    with open("decode.txt","r") as f:
        text = f.read()
        output = ""
        for i in range(0,26):
            for c in text:
                if c.upper() in alphabet:
                    output += alphabet[(alphabet.index(c) + i)%26]
                elif c == " ":
                    output += " "

            print(output + " " + str(i) + "\n")
            output = ""
        f.close()

def enc(key):
    with open("encode.txt","r") as f:
        output = ""
        text = f.read();
        for c in text:
            if c.upper() in alphabet:
                output += alphabet[(alphabet.index(c.upper()) + key) % 26]
            elif c == " ":
                output += " "
        print(output)
        output = " "
    f.close()


enc(25)




