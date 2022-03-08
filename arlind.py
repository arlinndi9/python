
print("1.Avoids""\n"
"2.Uses only""\n"
"3.Uses all""\n"
"4.Abecedarians""\n"
"5.Palindromes""\n")

chose_number=int(input("Choose a number between 1 and 6: "))
if chose_number ==1:
    f = open("../arlind3/word", 'r')
    letters = str(input("Enter forbidden letter: "))
    for word in f:
        s = [char for char in word if char not in (letters)]
        print(''.join(s))


elif chose_number==2:
    f = open("../arlind3/word", 'r')
    letters = str(input(" Uses only "))
    for word in f:
        s = [char for char in word if char in (letters)]
        print(''.join(s))

elif chose_number==3:
    letters = input('letters: ')
    f = open('../arlind3/word')
    for word in f:
        if all(x in word for x in letters):
            print(word)

elif chose_number==4:
    def is_abecedarian(word):
        prev = word[0]
        for i in word:
            if i < prev:
                return False
            else:
                prev = i
        return True

    f = open('../arlind3/word')
    for line in f:
        word = line.strip()
        if is_abecedarian(word):
            print(word)







elif chose_number==5:
        f = open('../arlind3/word')
        for line in f:
            line = line.strip()
            line2 = line[::-1]
            if line == line2:
                print(line)









