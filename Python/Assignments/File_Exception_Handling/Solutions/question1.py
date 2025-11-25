file_path = r"D:\Machine-Learning-Prime\Python\Assignments\File_Exception_Handling\Solutions\names.txt"

# Write 5 names to file
with open(file_path, 'w') as f:
    count = 1
    while count < 6:
        f.write(input("Enter name: ") + "\n")
        count += 1

# Read and print names
with open(file_path, 'r') as f:
    data = f.read()
    print("\nNames in the file:")
    print(data)
