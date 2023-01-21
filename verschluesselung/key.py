print("Bitte geben Sie den Schlüssel ein:")
schlüssel = input()

print("Bitte geben Sie den verschüsselten Text ein:")
keytext = input()


def entschluesselung(tname, schlüssel):
    key = ""
    for i in range(0,len(tname),1):
        for u in range(0,len(tname)+4,4):
            if tname[i:u] == str(schlüssel[0:4]):
                key += "a"
            elif tname[i:u] == str(schlüssel[4:8]):
                key += "b"
            elif tname[i:u] == str(schlüssel[8:12]):
                key += "c"
            elif tname[i:u] == str(schlüssel[12:16]):
                key += "d"
            elif tname[i:u] == str(schlüssel[16:20]):
                key += "e"
            elif tname[i:u] == str(schlüssel[20:24]):
                key += "f"
            elif tname[i:u] == str(schlüssel[24:28]):
                key += "g"
            elif tname[i:u] == str(schlüssel[28:32]):
                key += "h"
            elif tname[i:u] == str(schlüssel[32:36]):
                key += "i"
            elif tname[i:u] == str(schlüssel[36:40]):
                key += "j"
            elif tname[i:u] == str(schlüssel[40:44]):
                key += "k"
            elif tname[i:u] == str(schlüssel[44:48]):
                key += "l"
            elif tname[i:u] == str(schlüssel[48:52]):
                key += "m"
            elif tname[i:u] == str(schlüssel[52:56]):
                key += "n"
            elif tname[i:u] == str(schlüssel[56:60]):
                key += "o"
            elif tname[i:u] == str(schlüssel[60:64]):
                key += "p"
            elif tname[i:u] == str(schlüssel[64:68]):
                key += "q"
            elif tname[i:u] == str(schlüssel[68:72]):
                key += "r"
            elif tname[i:u] == str(schlüssel[72:76]):
                key += "s"
            elif tname[i:u] == str(schlüssel[76:80]):
                key += "t"
            elif tname[i:u] == str(schlüssel[80:84]):
                key += "u"
            elif tname[i:u] == str(schlüssel[84:88]):
                key += "v"
            elif tname[i:u] == str(schlüssel[88:92]):
                key += "w"
            elif tname[i:u] == str(schlüssel[92:96]):
                key += "x"
            elif tname[i:u] == str(schlüssel[96:100]):
                key += "y"
            elif tname[i:u] == str(schlüssel[100:104]):
                key += "z"
            elif tname[i:u] == str(schlüssel[104:108]):
                key += "ß"
            elif tname[i:u] == str(schlüssel[108:112]):
                key += " "
            elif tname[i:u] == str(schlüssel[112:116]):
                key += ","
            elif tname[i:u] == str(schlüssel[116:120]):
                key += "."
            elif tname[i:u] == str(schlüssel[120:124]):
                key += "?"
            elif tname[i:u] == str(schlüssel[124:128]):
                key += "!"
    return key


text = entschluesselung(keytext, schlüssel)

print(text)

input()