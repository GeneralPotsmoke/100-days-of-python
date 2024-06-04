import os

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print("File content:")
    print(content)

# Writing to a file
with open("output.txt", "w") as file:
    file.write("This is an output file.")

# Listing all files in a directory
directory = "."
files = os.listdir(directory)
print("Files in directory:")
print(files)
