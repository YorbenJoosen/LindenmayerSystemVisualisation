import turtle

# Make a startstring
string = "F[+F]-F[+F[+F]-F]-F[+F]-F[+F[+F]-F[+F[+F]-F]-F[+F]-F]-F[+F]-F[+F[+F]-F]-F[+F]-F[+F[+F]-F[+F[+F]-F]-F[+F]-F[+F[+F]-F[+F[+F]-F]-F[+F]-F]-F[+F]-F[+F[+F]-F]-F[+F]-F]-F[+F]-F[+F[+F]-F]-F[+F]-F[+F[+F]-F[+F[+F]-F]-F[+F]-F]-F[+F]-F[+F[+F]-F]-F[+F]-F"

string2 = """F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F+++++F++F++F+++++F-F++F-F++F++F+++++F-F++F++F++F++F+++++F-F++F
++F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F+++++F++F++F+++++F-F++F-F++F++F+++++F-F++F++F++F++F+++++F-F+
+F++F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F+++++F++F++F+++++F-F++F-F++F++F+++++F-F++F++F++F++F+++++F- 
F++F+++++F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F+++++F++F++F+++++F-F++F-F++F++F+++++F-F++F++F++F++F++ 
+++F-F++F-F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F+++++F++F++F+++++F-F++F-F++F++F+++++F-F++F++F++F++F+
++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F+++++F++F++F+++++F-F++F-F++F++F+++++F-F++F++F++F++
F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F+++++F++F++F+++++F-F++F-F++F++F+++++F-F++F++F++F
++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F+++++F++F++F+++++F-F++F-F++F++F+++++F-F++F++F+
+F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F+++++F++F++F+++++F-F++F-F++F++F+++++F-F++F++
F++F++F+++++F-F++F+++++F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F+++++F++F++F+++++F-F++F-F++F++F+++++F-F
++F++F++F++F+++++F-F++F-F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F+++++F++F++F+++++F-F++F-F++F++F+++++F-
F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F+++++F++F++F+++++F-F++F-F++F++F+++++
F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F+++++F++F++F+++++F-F++F-F++F++F+++
++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F+++++F++F++F+++++F-F++F-F++F++F+
++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F+++++F++F++F+++++F-F++F-F++F++
F+++++F-F++F++F++F++F+++++F-F++F+++++F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F+++++F++F++F+++++F-F++F-F
++F++F+++++F-F++F++F++F++F+++++F-F++F-F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F+++++F++F++F+++++F-F++F-
F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F+++++F++F++F+++++F-F++
F-F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F+++++F++F++F+++++F-F
++F-F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F+++++F++F++F+++++F
-F++F-F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F+++++F++F++F++++
+F-F++F-F++F++F+++++F-F++F++F++F++F+++++F-F++F+++++F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F+++++F++F++
F+++++F-F++F-F++F++F+++++F-F++F++F++F++F+++++F-F++F-F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F+++++F++F+
+F+++++F-F++F-F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F+++++F++
F++F+++++F-F++F-F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F+++++F
++F++F+++++F-F++F-F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F++++
+F++F++F+++++F-F++F-F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F++
+++F++F++F+++++F-F++F-F++F++F+++++F-F++F++F++F++F+++++F-F++F+++++F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F
++F+++++F++F++F+++++F-F++F-F++F++F+++++F-F++F++F++F++F+++++F-F++F-F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-
F++F+++++F++F++F+++++F-F++F-F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++F-F++F++F++F++F+++++
F-F++F+++++F++F++F+++++F-F++F-F++F++F+++++F-F++F++F++F++F+++++F-F++F"""


def draw(turtle_variable, string_variable, length, angle):
    stack = []
    for character in string_variable:
        # If it's [ we need to store the position and heading using a stack
        if character == "[":
            stack.append(turtle_variable.pos())
            stack.append(turtle_variable.heading())
        # If it's ] we move pop the heading and position out of the stack so we can move back to the old position
        elif character == "]":
            # Do penup because otherwise it will draw when moving to the old postion
            turtle_variable.penup()
            heading = stack.pop()
            turtle_variable.setheading(heading)
            position = stack.pop()
            turtle_variable.setposition(position[0], position[1])
            # Do pendown so the next line will be drawn
            turtle_variable.pendown()
        # If it's + we need to angle to the left
        elif character == "+":
            turtle_variable.left(angle)
        # If it's - we angle to the left
        elif character == "-":
            turtle_variable.right(angle)
        # If it's F we just need to draw a line
        elif character == "F":
            turtle_variable.forward(length)


# Initialize turtle
turtleVariable = turtle.Turtle()
# Initialize a window
window = turtle.Screen()
# Turn the window black
window.bgcolor("black")
# Make the color of the lines orange
turtleVariable.color("orange")
# Make the pensize 1
turtleVariable.pensize(1)
# Do penup so we can move to the starting position without drawing lines
turtleVariable.penup()
# Move to the starting position
turtleVariable.setpos(0,0)
# Do pendown so we can start drawing
turtleVariable.pendown()
# Set the speed
turtleVariable.speed(-100)
# Turtle starts horizontally, but we want to start upwards so we angle 90 degrees to the left
turtleVariable.left(180)
# Call the drawfunction
draw(turtle_variable=turtleVariable,
     string_variable=string2,
     length=10,
     angle=36)
# Say the window only closes when we click otherwise it closes after the drawing is done and we can't take a good look at it
window.exitonclick()
