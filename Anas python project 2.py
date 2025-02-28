import turtle


tom = turtle.Turtle()
turtle.bgcolor("black")
tom.speed(0)  
tom.color('sky blue')

for i in range(100):
    for i in range(4):
        tom.fd(280)
        tom.rt(90)
    tom.rt(360/100)

tom.pu()
tom.goto(0,0)
tom.pd()
tom.pensize(5)
for i in range(360):
    tom.color('black')
    tom.fd(277)
    tom.bk(277)
    tom.lt(360/360)
tom.pu()
tom.goto(0,0)
tom.pd()
tom.pensize(1)


tom.color('red')
for i in range(100):
    for i in range(4):
        tom.fd(197)
        tom.rt(90)
    tom.rt(360/100)


tom.pu()
tom.goto(0,0)
tom.pd()
tom.pensize(5)
for i in range(360):
    tom.color('black')
    tom.fd(194)
    tom.bk(194)
    tom.lt(360/360)


tom.color('sky blue')
tom.pensize(1)

for i in range(100):
    for i in range(4):
        tom.fd(137)
        tom.rt(90)
    tom.rt(360/100)


tom.pensize(5)
for i in range(360):
    tom.color('black')
    tom.fd(134)
    tom.bk(134)
    tom.lt(360/360)


tom.pensize(1)
tom.color('red')
for i in range(100):
    for i in range(4):
        tom.fd(95)
        tom.rt(90)
    tom.rt(360/100)


tom.pensize(5)
for i in range(360):
    tom.color('black')
    tom.fd(92)
    tom.bk(92)
    tom.rt(360/360)
    
        
    
  

