
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
PTables = PrettyTable()

PTables = PrettyTable()
PTables.field_names = ["Selection No.", "Weapon Name", "Damage"]
PTables.add_row(["0", "Fist", "1 dp"])
PTables.add_row(["1", "Knuckle Busters", "2.5 dp"])
PTables.add_row(["2", "Cheap Knife", "5 dp"])
PTables.add_row(["3", "Wooden Baton", "6 dp"])
print(PTables)
