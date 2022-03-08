def before_last(str):
    length = len(str)
    last_char = str[length - 2]
    return last_char

print(before_last("riinvest"))


def find(word, letter, index):
    for index in range(index, len(word)):
        if word[index] == letter:
            return index
    return -1

print(find("pristine","i",4))

def remove_i(word,index):
    if len(word)>index:
        return word[0:index:]+word[index+1::]

print(remove_i("lepri",2))




