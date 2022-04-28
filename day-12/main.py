
# from turtle import Turtle, Screen

# tim = Turtle()
# print(tim)
# tim.shape("turtle")
# tim.color("red")

# tim.forward(100)

# my_screen = Screen()
# print(my_screen.canvheight)

# my_screen.exitonclick()

from prettytable import PrettyTable

x = PrettyTable()
x.add_column("Pokemon Name", ["Pikachu", "Squirtle"])
x.add_column("Type", ["Electric", "Water"])

print(x)