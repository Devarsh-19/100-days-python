
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

x.add_column("Genre", ["Action", "Romance", "Horror"])
x.add_column("Name",["Naruto", "Your Name", "Parasyte"])

x.align = "l"

print(x)