import math

def sub(a,b):
   return a-b

sub(5,2)

def fl(a):
    if a==2.0:
        return 1
    else:
        return -1

fl(2.0)


def my_sqrt(b):
    return math.sqrt(b)

my_sqrt(81)

def cosine(b):
    return math.cos(b)
cosine(3)

def even_sum(number):
    if number %2==1:
        number-=1
    if (number < 1):
         return 0
    return number+even_sum(number-2)


print(even_sum(5))