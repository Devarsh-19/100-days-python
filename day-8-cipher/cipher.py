def shift(s,k):
    nw = ""
    for i in s:
        
        nw +=(chr(ord(i) + k))
        
    return nw


str = input("Enter the text: ")
k = int(input("Enter the shift: "))
print(shift(str,k))