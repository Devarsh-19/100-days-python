def check(num):
    
    for x in range(2,num):
        if num % x == 0:
            return "Not prime"
    
    return "Prime no."

n = int(input("Enter a number: "))
print(check(num = n))    