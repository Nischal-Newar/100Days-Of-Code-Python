# import modules
from turtle import Screen, Turtle
import random

# setup screen and betting input
screen = Screen()
screen.setup(width=900, height=800)
screen.colormode(255)
screen.bgcolor("#4D7F7B")
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race (red, orange, yellow, "
                                                          "green, blue, purple)? Enter a color: ")

# declare turtle name and colors
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_name = ["Anju", "Asuka", "Daisuke", "Hana", "Lucy", "Miyuki"]

# loop through turtle_name, create objects and assign the different states
x_index = -440
y_index = 300
for index in range(len(turtle_name)):
    turtle_name[index] = Turtle(shape="turtle")
    turtle_name[index].penup()
    turtle_name[index].color(colors[index])
    turtle_name[index].setposition(x=x_index, y=y_index)
    y_index -= 100

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_name:
        if is_race_on:
            if turtle.xcor() > 410:
                is_race_on = False
                winning_color = turtle.pencolor()
                if user_bet == winning_color:
                    print(f"You've guessed correct! The {winning_color} turtle is the winner!")
                else:
                    print(f"Oops! You've lost. The {winning_color} turtle is the winner")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


# exit the screen
screen.exitonclick()
