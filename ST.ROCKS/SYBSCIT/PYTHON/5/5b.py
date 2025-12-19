print("Name: Shekhar Suman")
print("Roll No: 48")

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

result = {**dic1, **dic2, **dic3}
print(result)