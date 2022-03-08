



#1. Write a program that reads words.txt and prints only the words with
#more than 20 characters (not counting whitespace).

fin=open('../arlind3/word')
for word in fin:
    my_word=word.strip()
    if len(my_word)<4:
        print(my_word)


'''1. Write a function called has_no_e that returns True if the given
word doesn’t have the letter “e” in it.
2. Write a program that reads words.txt and prints only the words
that have no “e”.
3. Compute the percentage of words in the list that have no “e”.
'''
def has_no_e(word):
  for letter in word:
      if letter == 'e':
         return False
  return True

fin = open('../arlind3/word')
all_words, no_e_words = 0, 0
for line in fin:
  word = line.strip()
  all_words += 1
  if has_no_e(word):
       print(word)
       no_e_words += 1

print("\nPercentage of words that have no e: {:.0%}".format(no_e_words/all_words))
fin.close()

'''1. Write a function named avoids that takes a word and a string of
forbidden letters, and that returns True if the word doesn’t use any of
the forbidden letters.
2. Write a program that prompts the user to enter a string of forbidden
letters and then prints the number of words that don’t contain any of
them.'''

def avoids(word, forbidden):
    for letter in word:
       if letter in forbidden:
         return False
    return True

fin = open('../arlind3/word')
forbiddens = input("> Please give the forbidden letters: ")

for line in fin:
   word = line.strip()
   if avoids(word, forbiddens):
     print(word)


''' Write a function named uses_only that takes a word and a string
of letters, and that returns True if the word contains only letters in the
list.'''

def uses_only(word, available):
    for letter in word:
       if letter not in available:
         return False
    return True