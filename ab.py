def avoid(word,forbidden):
    for l in word:
        if l in forbidden:
            return False
    return True

def savoid(forbiddens):
    total=0
    f=open('word')
    for l in f:
        word=l.strip()
        if avoid(word,forbiddens):
            total=total+1
            if total<20:
                print(word)
    return total

def useonly(word,available):
    for l in word:
        if l not in available:
            return False
    return True

def suseonly(available):
    total = 0
    f = open('word')
    for l in f:
        word = l.strip()
        if useonly(word, available):
            total = total + 1
            if total < 20:
                print(word)
    return total


def useall(word,required):
    for l in required:
        if l not in word:
            return False
    return True

def suseall(required):
    total = 0
    f = open('word')
    for l in f:
        word = l.strip()
        if useall(word, required):
            total = total + 1
            if total < 20:
                print(word)
    return total

def abecedarian(word):
    prev=word[0]
    for c in word:
        if c<prev:
            return False
        prev=c
    return True

def sabecedarian():
    total = 0
    f = open('word')
    for l in f:
        word = l.strip()
        if abecedarian(word):
            total = total + 1
            if total < 20:
                print(word)
    return total

def palindrome(word):
    i = 0
    j = len(word) - 1
    while i < j:
        if word[i] != word[j]:
            return False
        i = i + 1
        j = j - 1
    return True

def spalindrome():
    total = 0
    f = open('word')
    for l in f:
        word = l.strip()
        if palindrome(word):
            total = total + 1
            if total < 20:
                print(word)
    return total

print("1.Avoids""\n"
"2.Uses only""\n"
"3.Uses all""\n"
"4.Abecedarians""\n"
"5.Palindromes""\n")

chose_number=int(input("Choose a number between 1 and 6: "))
if chose_number==1:
    letters = (input("Enter forbidden letter: "))
    f=open('word')
    print(avoid)
