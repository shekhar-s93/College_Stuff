def read_last_n_lines(file_path, n):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        last_n_lines = lines[-n:]
        return last_n_lines

file_path = r"C:\Users\SHEKHAR SUMAN\Desktop\PY EXAM\PRACTICAL\TEXT FILE\textfile.txt"
n = 3  
last_lines = read_last_n_lines(file_path, n)

for line in last_lines:
    print(line.strip())
