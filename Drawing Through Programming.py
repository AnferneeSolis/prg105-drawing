import turtle

def square(bob,length):
    bob.fd(100)
    bob.lt(90)
    bob.fd(length)
    bob.lt(90)
    bob.fd(length)
    bob.lt(90)
    bob.fd(length)
    bob.lt(90)
    bob.fd(100)
def triangle(sam,distance):
    sam.pu()
    sam.fd(distance)
    sam.lt(90)
    sam.fd(200)
    sam.pd()
    sam.lt(30)
    sam.fd(200)
    sam.lt(120)
    sam.fd(200)
def rectangle(bill,height):
    bill.pu()
    bill.fd(35)
    bill.pd()
    bill.lt(90)
    bill.fd(height)
    bill.rt(90)
    bill.fd(45)
    bill.rt(90)
    bill.fd(height)
def window(joe):
    joe.pu()
    joe.bk(25)
    joe.lt(90)
    joe.fd(25)
    joe.pd()
    joe.fd(50)
    joe.lt(90)
    joe.fd(50)
    joe.lt(90)
    joe.fd(50)
    joe.lt(90)
    joe.fd(50)
def top_left(will):
    will.pu()
    will.bk(25)
    will.lt(90)
    will.fd(125)
    will.pd()
    will.fd(50)
    will.lt(90)
    will.fd(50)
    will.lt(90)
    will.fd(50)
    will.lt(90)
    will.fd(50)
def top_right(rick):
    rick.pu()
    rick.fd(25)
    rick.lt(90)
    rick.fd(125)
    rick.pd()
    rick.fd(50)
    rick.rt(90)
    rick.fd(50)
    rick.rt(90)
    rick.fd(50)
    rick.rt(90)
    rick.fd(50)

bob = turtle.Turtle()
sam = turtle.Turtle()
bill = turtle.Turtle()
joe = turtle.Turtle()
will = turtle.Turtle()
rick = turtle.Turtle()

square(bob,200)
triangle(sam,100)
rectangle(bill,75)
window(joe)
top_left(will)
top_right(rick)

turtle.done()
