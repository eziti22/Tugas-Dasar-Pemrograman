words = 'ABDCEFGHIJKLMNOPQRSTUVWXYZ'
def countUppercase(kalimat):
    total = 0
    for char in kalimat:
        if char.isupper():
            total += 1
    return total

def countUppercase2(kalimat):
    total = 0
    for i in range(len(kalimat)):
        for j in range(len(words)):
            if kalimat[i] == words[j]:
                total += 1
    return total