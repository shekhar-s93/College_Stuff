print("Name: Shekhar Suman")
print("Roll No: 48")
def armstrong(num):
    digit= str(num)
    num_digit= len(digit)
    sop= sum(int(digit)**num_digit for digit in digit)
    return sop== num
input= int(input("Enter a number: "))

if armstrong(input):
           print("This is a armstrong number")
else:
    print("This is not an armstrong number")