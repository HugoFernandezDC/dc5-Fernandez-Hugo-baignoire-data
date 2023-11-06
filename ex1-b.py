phrase = input("phrase : ")

phrase_maj = ""

for lettre in phrase:
    if 'a' <= lettre <= 'z':
        maj = chr(ord(lettre) - 32)
        phrase_maj += maj
    else:
        phrase_maj += lettre

phrase_min = ""

for lettre in phrase:
    if 'A' <= lettre <= 'Z':
        min = chr(ord(lettre) + 32)
        phrase_min += min
    else:
        phrase_min += lettre

mots = phrase.split()
nombre_mots = len(mots)

print(phrase_maj)
print(phrase_min)
print(nombre_mots)
