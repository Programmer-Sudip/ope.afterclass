# Task 1: Open the file and print the contents of the file
file = open('example.txt', 'r')
contents = file.read()
print("Contents of the file:")
print(contents)
file.close()

# Task 2: Open the file again to print the first ten characters
file = open('example.txt', 'r')
first_ten_chars = file.read(10)
print("\nFirst ten characters of the file:")
print(first_ten_chars)
file.close()

# Task 3: Open the file again to print the first line of the file
file = open('example.txt', 'r')
first_line = file.readline()
print("\nFirst line of the file:")
print(first_line.strip())
file.close()

# Task 4: Open the file again to print the first four lines of the file
file = open('example.txt', 'r')
print("\nFirst four lines of the file:")
for _ in range(4):
    line = file.readline()
    print(line.strip())
file.close()

# Task 5: Open the file again to loop through the contents and print all lines one by one
file = open('example.txt', 'r')
lines = file.readlines()
print("\nAll lines in the file:")
for line in lines:
    print(line.strip())
file.close()
