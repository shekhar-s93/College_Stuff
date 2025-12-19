print("Name: Shekhar Suman")
print("Roll No: 48")

my_dict = {'Pears':32, 'DragonFruits':23, 'CusturdApple':50, 'pomegranade': 5}
sorted_asc = dict(sorted(my_dict.items(), key=lambda item: item[1]))
sorted_desc = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

print("Ascending order: ", sorted_asc)
print("Descending order: ", sorted_desc)