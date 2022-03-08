import turtle

t=turtle.Turtle()


def curves(t,num):
   for i in range(num):

        t.fd(100)
        t.lt(90)
        t.fd(20)
        t.lt(90)
        t.fd(100)
        t.rt(90)
        t.fd(20)
        t.rt(90)





curves(t,3)


def upstair(t,num):
    for i in range(num):
        t.fd(50)
        t.lt(90)
        t.fd(50)
        t.rt(90)


#upstair(t,5)





def right_triangle(t,l):
    for i in range(1):
        t.fd(l)
        t.lt(90)
        t.fd(l)
        t.lt(135)
        t.fd(l*1.5)


#right_triangle(t,100)





turtle.mainloop()