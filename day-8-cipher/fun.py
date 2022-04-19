

# def greet(name, roll):
#     print(f"Hello {name}")
#     print(f"Roll no = {roll}")
    
# greet(roll=54, name= "a")

from math import ceil

def calc_area(h, w, c):
    ar = (h * w)  / c
    return ceil(ar)
    

test_h = int(input("Enter height : "))
test_w = int(input("Enter width : "))
coverage = 5


print(calc_area(h=test_h, w=test_w, c=coverage))
