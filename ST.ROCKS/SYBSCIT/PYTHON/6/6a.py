print("Name: Shekhar Suman")
print("Roll No: 48")

file_path = r"C:\Users\SHEKHAR SUMAN\Desktop\PY EXAM\PRACTICAL\TEXT FILE\textfile.txt"

with open(file_path, 'r') as file:
    content = file.read()

print(content)
