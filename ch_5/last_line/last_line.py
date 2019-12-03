
#Option 1
def get_last_line():
    file = input("Enter the name of a file: ")
    while True:
        try:
            with open(file, mode='r') as f_object:
                rows = f_object.readlines()
                for row in rows:
                    total_rows = row.split("\n")
                return total_rows[-1]
                break
        except OSError:
            print("The file is not found.")
            file = input("Enter the name of a file: ")

print(get_last_line())

#Option 2:

def get_last_line(filename):
    for line in open(filename):
        current_line = line
    return current_line
print(get_last_line('text_file.txt'), end='')
