a = str(input("Name:"))
b = str(input("Age:"))
c = str(input("Address:"))
d = a,b,c

if (b is not int):
    print("Age is Invalid")
else:
    print(a)    
    print(b)
    print(c)