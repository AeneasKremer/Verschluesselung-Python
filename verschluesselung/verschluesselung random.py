#Liabries and lists
import random
random.seed
import time
schlüssel = []

#function
def listausgabe(liste,):
    counter = 0
    for temp in liste:
        counter += 1
        print(counter)
        print(temp)

#creation of the key
counter = 0
while counter < 32:
    r = random.randint(1000,9999)
    if r != schlüssel:
        schlüssel.append(r)
        counter += 1

#Verschlüsselung
def verschluesselung(tname, schlüssel):
    key = ""
    for i in range(0,len(tname),1):
        if tname[i] == "a" or tname[i] == "A":
            key += str(schlüssel[0])
        elif tname[i] == "b" or tname[i] == "B":
            key += str(schlüssel[1])
        elif tname[i] == "c" or tname[i] == "C":
            key += str(schlüssel[2])
        elif tname[i] == "d" or tname[i] == "D":
            key += str(schlüssel[3])
        elif tname[i] == "e" or tname[i] == "E":
            key += str(schlüssel[4])
        elif tname[i] == "f" or tname[i] == "F":
            key += str(schlüssel[5])
        elif tname[i] == "g" or tname[i] == "G":
            key += str(schlüssel[6])
        elif tname[i] == "h" or tname[i] == "H":
            key += str(schlüssel[7])
        elif tname[i] == "i" or tname[i] == "I":
            key += str(schlüssel[8])
        elif tname[i] == "j" or tname[i] == "J":
            key += str(schlüssel[9])
        elif tname[i] == "k" or tname[i] == "K":
            key += str(schlüssel[10])
        elif tname[i] == "l" or tname[i] == "L":
            key += str(schlüssel[11])
        elif tname[i] == "m" or tname[i] == "M":
            key += str(schlüssel[12])
        elif tname[i] == "n" or tname[i] == "N":
            key += str(schlüssel[13])
        elif tname[i] == "o" or tname[i] == "O":
            key += str(schlüssel[14])
        elif tname[i] == "p" or tname[i] == "P":
            key += str(schlüssel[15])
        elif tname[i] == "q" or tname[i] == "Q":
            key += str(schlüssel[16])
        elif tname[i] == "r" or tname[i] == "R":
            key += str(schlüssel[17])
        elif tname[i] == "s" or tname[i] == "S":
            key += str(schlüssel[18])
        elif tname[i] == "t" or tname[i] == "T":
            key += str(schlüssel[19])
        elif tname[i] == "u" or tname[i] == "U":
            key += str(schlüssel[20])
        elif tname[i] == "v" or tname[i] == "V":
            key += str(schlüssel[21])
        elif tname[i] == "w" or tname[i] == "W":
            key += str(schlüssel[22])
        elif tname[i] == "x" or tname[i] == "X":
            key += str(schlüssel[23])
        elif tname[i] == "y" or tname[i] == "Y":
            key += str(schlüssel[24])
        elif tname[i] == "z" or tname[i] == "Z":
            key += str(schlüssel[25])
        elif tname[i] == "ß":
            key += str(schlüssel[26])
        elif tname[i] == " ":
            key += str(schlüssel[27])
        elif tname[i] == ",":
            key += str(schlüssel[28])
        elif tname[i] == ".":
            key += str(schlüssel[29])
        elif tname[i] == "?":
            key += str(schlüssel[30])
        elif tname[i] == "!":
            key += str(schlüssel[31])
    return key

#Entschlüsselung
def entschluesselung(tname, schlüssel):
    key = ""
    for i in range(0,len(tname),1):
        for u in range(0,len(tname)+4,4):
            if tname[i:u] == str(schlüssel[0]):
                key += "a"
            elif tname[i:u] == str(schlüssel[1]):
                key += "b"
            elif tname[i:u] == str(schlüssel[2]):
                key += "c"
            elif tname[i:u] == str(schlüssel[3]):
                key += "d"
            elif tname[i:u] == str(schlüssel[4]):
                key += "e"
            elif tname[i:u] == str(schlüssel[5]):
                key += "f"
            elif tname[i:u] == str(schlüssel[6]):
                key += "g"
            elif tname[i:u] == str(schlüssel[7]):
                key += "h"
            elif tname[i:u] == str(schlüssel[8]):
                key += "i"
            elif tname[i:u] == str(schlüssel[9]):
                key += "j"
            elif tname[i:u] == str(schlüssel[10]):
                key += "k"
            elif tname[i:u] == str(schlüssel[11]):
                key += "l"
            elif tname[i:u] == str(schlüssel[12]):
                key += "m"
            elif tname[i:u] == str(schlüssel[13]):
                key += "n"
            elif tname[i:u] == str(schlüssel[14]):
                key += "o"
            elif tname[i:u] == str(schlüssel[15]):
                key += "p"
            elif tname[i:u] == str(schlüssel[16]):
                key += "q"
            elif tname[i:u] == str(schlüssel[17]):
                key += "r"
            elif tname[i:u] == str(schlüssel[18]):
                key += "s"
            elif tname[i:u] == str(schlüssel[19]):
                key += "t"
            elif tname[i:u] == str(schlüssel[20]):
                key += "u"
            elif tname[i:u] == str(schlüssel[21]):
                key += "v"
            elif tname[i:u] == str(schlüssel[22]):
                key += "w"
            elif tname[i:u] == str(schlüssel[23]):
                key += "x"
            elif tname[i:u] == str(schlüssel[24]):
                key += "y"
            elif tname[i:u] == str(schlüssel[25]):
                key += "z"
            elif tname[i:u] == str(schlüssel[26]):
                key += "ß"
            elif tname[i:u] == str(schlüssel[27]):
                key += " "
            elif tname[i:u] == str(schlüssel[28]):
                key += ","
            elif tname[i:u] == str(schlüssel[29]):
                key += "."
            elif tname[i:u] == str(schlüssel[30]):
                key += "?"
            elif tname[i:u] == str(schlüssel[31]):
                key += "!"
    return key

#Listenausgabe
def listausgabe(list):
    for temp in list:
        print(temp, end="")

#Ausgabe
print("Bitte geben Sie einen Text ein:")
eingabe = input()
key = verschluesselung(eingabe, schlüssel)
print(120 * "_")
print("Verschlüsselter Text:", key)
text = entschluesselung(key, schlüssel)
print(120 * "_")
print("Schlüssel:")
listausgabe(schlüssel)
print()
print(120 * "_")
time.sleep(5)
print("Drücken Sie Eingabe um das Programm zu beenden!")
input()

