#1
import turtle


def right_justify(s):
    print(s.rjust(70," "))

right_justify("monty")

#2
t=turtle.Turtle()
def square_labyrinth(t,n):
    for i in range(n*4):
        t.fd(i*10)
        t.right(90)

#square_labyrinth(t,5)



#3
def triangle_labyrinth(t,n):
    for i in range(n*3):
        t.rt(120)
        t.bk(i*10)


#triangle_labyrinth(t,6)

turtle.mainloop()


#4
def do_it(a,b,fun):
    if fun=="add":
        return a+b
    elif fun=="sub":
        return a-b
    elif fun=="mult":
        return a*b
    elif fun=="div":
        return a/b
    else:
        return "Not suitable function"

do_it(5,2,"div")

#5
def add_some(num,step):
      if step <= 0:
        print("step should be greater than zero")
      else:
        sum = 0
        while (num > 0):
            sum += num
            num -= step
        return sum

add_some(4,2)



