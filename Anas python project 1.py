import turtle


tom = turtle.Turtle()
turtle.bgcolor("black")
tom.speed(0)  
tom.hideturtle() 


turtle.colormode(255)

# Define square hole size
hole_size = 40  # Adjust this for a bigger or smaller hole

# Spiral with a square hole
for i in range(274):
    red_value = max(255 - i, 150)  # Starts from yellow (255,255,0) to light green (150,255,0)
    green_value = 255  # Always full green for brightness
    
    tom.pencolor(red_value, green_value, 0)  # (R, G, B) - Yellow to Light Green transition

    # Check if inside the hole area
    x, y = tom.pos()
    if abs(x) > hole_size / 2 or abs(y) > hole_size / 2:
        tom.pendown()  # Draw only outside the square hole
    else:
        tom.penup()  # Lift the pen inside the hole area

    tom.forward(i * 2)
    tom.right(91)

turtle.done()
