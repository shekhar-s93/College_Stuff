print("Name: Shekhar Suman")
print("Roll No: 48")
def member (list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False
list1 = [32,22,66,81]
list2 = [55,66,69,91]
print(member(list1, list2))