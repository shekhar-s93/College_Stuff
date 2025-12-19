print("Name: Shekhar Suman")
print("Roll No: 48")

file_path = r"C:\Users\SHEKHAR SUMAN\Desktop\PY EXAM\PRACTICAL\TEXT FILE\textfile.txt"

text_to_append = "\nHi Shekhar this is your append text."

with open(file_path, 'a') as file:
    file.write(text_to_append)

with open(file_path, 'r') as file:
    updated_content = file.read()

print(updated_content)
