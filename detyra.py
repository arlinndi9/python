
#1
def square_root(number):
    print(number**0.5)

square_root(80)
#2
def call_function():
    square_root(100)
    square_root(200)
    square_root(300)

call_function()

#3
def two_arguments(a,b):
    mbledhja=a+b
    print(mbledhja)
    square_root(mbledhja)
    difference=a-b
    print(difference)
    square_root(difference)
    product=a*b
    print(product)
    square_root(product)
    quotient=a/b
    print(quotient)
    square_root(quotient)

two_arguments(10,2)

#4
def printoje():
    print("python")

printoje()


#5
def printo_four_times(tekst):
    print(tekst)
    print(tekst)
    print(tekst)
    print(tekst)
printo_four_times("Arlind")

#6
def print_type(a,b):
    print(type(a))
    print(type(b))
print_type("arlind",6)

import turtle

ar=turtle.Turtle()

def star(ar,forward,right):
    for i in range(5):
        ar.fd(forward)
        ar.rt(right)

#star(ar,150,144)

def square(ar,forward,left):
    for i in range(4):
        ar.fd(forward)
        ar.lt(left)

#square(ar,100,90)

def polygon(ar,n,length):
    angle=360/n
    for i in range(n):
        ar.fd(length)
        ar.lt(angle)

polygon(ar,6,70)

my_str = "Dishroj-shum,-por...-nuk-po-dij"
word=my_str.split("-")
print(word)
my_str=' '.join(word)
print(word)