import turtle

string = "F[+F]-F[+F[+F]-F]-F[+F]-F[+F[+F]-F[+F[+F]-F]-F[+F]-F]-F[+F]-F[+F[+F]-F]-F[+F]-F"


def draw(turtle_variable, string_variable, length, angle):
    savePosition = turtle_variable.pos()
    for character in string_variable:
        if character == "¨[":
            savePosition = turtle_variable.pos()
        elif character == "]":
            turtle_variable.setpos(savePosition)
        elif character == "+":
            turtle_variable.left(angle)
        elif character == "-":
            turtle_variable.right(angle)
        elif character == "F":
            turtle_variable.forward(length)


turtleVariable = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("black")
turtleVariable.color("orange")
turtleVariable.pensize(1)
turtleVariable.penup()
turtleVariable.setpos(-250, -250)
turtleVariable.pendown()
turtleVariable.speed(0)
draw(turtle_variable=turtleVariable,
     string_variable=string,
     length=10,
     angle=45)
window.exitonclick()