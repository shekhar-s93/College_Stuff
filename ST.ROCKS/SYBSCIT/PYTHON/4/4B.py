print("Name: Shekhar Suman")
print("Roll No: 48")
my_list = ['s', 'h', 'e', 'k', 'h', 'a', 'r']
for index in sorted([0,2,4,5], reverse = True):
    my_list.pop(index)
print("Output: ",my_list)