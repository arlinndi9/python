import math


def product_or_sum(a,b):
    c=a*b

    if c<1000:
        print(c)

    else:
        print(a+b)

#product_or_sum(80,5)


def divisible_by_7_and_5(x,y):
    for i in range(x,y+1):
        if i%7==0 and i%5==0:
            print(i)

#divisible_by_7_and_5(1,100)

def div(n):
    for i in range(n):
        if n%2==0:
            print(n)
            break

#div(5)

def is_odd(num):
    if num%2==1:
        print("true")
    else:
        print("false")

#is_odd(9)



def fizzbuzz(number):
    for number in range(number):
         if number%3==0 and number%5==0:
             print("fizzbuzz")

         elif number%3==0:
            print("fizz")

         elif number%5==0:
            print("buzz")


#fizzbuzz(50)


def sub(a,b):
   return a-b

#print(sub(5,2))

def fl(a):
    #float_number=float(a)
    if a==2.0:
        return 1
    else:
        return -1

#print(fl(2.0))


def my_sqrt(b):
    return math.sqrt(b)


#print(my_sqrt(81))

def cosine(b):
    return math.cos(b)
#print(cosine(3))

def even_sum(number):
    if number %2==1:
        number-=1
    if (number < 1):
         return 0
    return number+even_sum(number-2)


#print(even_sum(5))


def add(a,b):
    return a+b
#print(add(5,2))

def ss(str):

    if str =="Po":
        return True
    else:
        return False

#print(ss("Po"))

def my_pow(b,p):
    return math.pow(b,p)

#print(my_pow(2,2))

def sine(b):

    return math.sin(b)

#print(sine(1.23))

def my_sum(num):
    total = 0
    for num in range(1, num + 1):
     total = total + num
    return total

#print(my_sum(9))

def odd_sum(num):
    if num %2==0:
        num-=1
    if (num < 1):
        return 0
    return num+odd_sum(num-2)
#print(odd_sum(5))



def even_sum(num):
    total = 0
    i = 0
    while (i < num):
        i=i+1
        if i %2==0:
          total = total + i
    return total

#print(even_sum(5))

def bb():
    while True:
        number = int(input("number: "))
        if number%7==0:
           break
        print(number)
#bb()

def my_sum(num):
    total=0
    i=0
    while(i<num+1):
        total=total+i
        i=i+1
    return total

print(my_sum(4))


def odd_sum(num):
   counter=0
   total=0
   while(counter<num):
       counter=counter+1
       if counter%2==1:
           total=total+counter
   print(total)
#odd_sum(5)

def br():
    while True:
        line=input("txt: ")
        if line=="ani":
            break
        print(line)

#br()

fruit="banana"
fruit[1]

print(len(fruit))

frutat="molla"
index=0
"""
while index<len(frutat):
    letter=frutat[index]
    print(letter)
    index=index+1
   """
def backward(s):
    index=-1
    while abs(index)<=len(s):
        print(s[index])
        index=index-1

backward("arlind")

for letter in frutat:
    print(letter)

prefix="jklmnopq"
suffix="ack"

for letter in prefix:
    if letter=="o" or letter=="q":
        print(letter+"u"+suffix)
    else:
        print(letter+suffix)

s="monty python"
print(s[0:5])#numri i pare  tregon prej cilit index me fillu ,numri i dyte ku me mbaru

def counter(word,shkronja):
    count=0
    for letter in word:
        if letter==shkronja:
            count=count+1
    print(count)

def strr(s):
    if len(s)<2:
        return ''
    elif len(s)>=2:
        return s[0:2]+s[len(s)-2:]


print(strr("Arlind"))

def to_uppercase(str1):
    num_upper = 0
    for letter in str1[:4]:
        if letter.upper() == letter:
            num_upper += 1
        else:
             return str1.lower()
    return str1

print(to_uppercase("Riinvest"))


def change_char(str1):
  char = str1[0]
  str1 = str1.replace(char, '$')
  str1 = char + str1[1:]

  return str1

print(change_char("kimik"))

astring="hello world!"
print(astring.count("l"))

name="arlind"
for letter in name:
    print(letter)

print('a' in name)

#slices
print(name[:3])

def find(word,letter):
    index=0
    while index<len(word):
        if word[index]==letter:
            print("shkronja e kerkuar gjendet ne indexin: ",index)#per concatinim ne mes stringut edhe variables perdoret presja(,)
        index=index+1


find("arlind","r")

def in_both(word1, word2):
      for letter in word1:
        if letter in word2:
            print(letter)

in_both("prishtine","prizren")

my_lista=[1,2.0,'my home',['pi','phi',3.13,1.617]]
my_lista[3][2]=3.14
my_lista[3][3]=1.618
print(my_lista)

floats=[1.0,3.0,4.0]
new_list = [x+1 for x in floats]
print(new_list)

my_list=['my home','our school']
sub_list=['time','next','The']
sub_list.sort()
print(sub_list)
my_list.append(sub_list)
print(my_list)
my_list.extend(sub_list)
print(my_list)

cities = ["Prishtinë", "Shqipni", "Azi", "Atlantik", "Pejë"]
countries = ["Kosovë", "Buna", "Drini", "Prizren"]
countries.append(cities.pop(1))
countries.append(cities.pop(1))
countries.append(cities.pop(1))
cities.append(countries.pop(1))
cities.append(countries.pop(1))
cities.append(countries.pop(1))
print("country:",countries)
print("cities",cities)

cities.remove("Buna")
cities.remove("Drini")
print(cities)

strings = ['a', 'c', [1.0, 2], 3, 4, 'AC', "AD", 1.0]
floats = [0.0, 2.0, 3.0, 9, "a string", "another string", 4.5]

del strings[2:5]
del floats[3:6]
print(floats)
floats.append(strings.pop(-1))
#floats.remove(9)
strings.append(floats.pop(3))
strings.append(floats.pop(3))

my_str = "Dishroj-shum,-por...-nuk-po-dij"
word=my_str.split("-")
print(word)
my_str=' '.join(word)
print(word)
