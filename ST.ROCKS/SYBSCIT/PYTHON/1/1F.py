print("Name: Shekhar Suman")
print("Roll No: 48")
def fact(n):
    if n == 1:
        return n
    else:
        return n*fact(n-1)
num=7
if num<0:
    print("Factorial does not exist for Negative numbers")
elif num==0:
    print("The factorial of 0 is 1")
else:
    print("The factorial is", fact(num))