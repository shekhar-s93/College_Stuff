print("Name: Shekhar Suman")
print("Roll No: 48")

def divided_numbers():
    try:
        num1 = float(input("Enter the Numerator: "))
        num2 = float(input("Enter the Denominator: "))        
        result = num1/num2
        
    except ValueError:
        print("Error: Please enter Numeric Value Only:")
        
    except ZeroDivisionError:
        print("Error: Division by zero in not allowed:")
        
    else:
        print(f"Try result is :{result}")
        
    finally:
        print("Executaion Completed.")
        
divided_numbers()