# Question 5
students = {}

def question5(choice):
    match choice:
        case 'A':
            stu = input("Enter student name: ")
            marks = int(input("Enter marks: "))
            students[stu] = marks
            print("Student added successfully.")

        case 'B':
            stu = input("Enter student name to update: ")
            if stu not in students:
                print(f"{stu} is not found.")
            else:
                marks = int(input("Enter new marks: "))
                students[stu] = marks
                print(f"Marks for {stu} updated successfully.")

        case 'C':
            stu = input("Enter student name to search: ")
            print(students.get(stu, "Student not found."))

        case 'D':
            print("All students and marks:")
            for name, mark in students.items():
                print(name, ":", mark)

        case _:
            print("Invalid choice.")
            

# print("You have 4 options (A,B,C,D)")
# print("Press A to Add a Student")
# print("Press B to Update marks of a student")
# print("Press C to Search for a student")
# print("Press D to Display all students and marks")
# print("Press Q to Quit")

# while True:
#     choice = input("Enter your choice: ").upper()
#     if choice == 'Q':
#         break
#     question5(choice)


# Question 6 : Given a list of words convert into dictionary where key is word and value is it's count

# words =["apple","banana","kiwi","cherry","mango"]

# dict = {}
# for word in words:
#     dict[word] = len(word)

# print(dict)


# Question7 : Write a program that takes a string from the user and prints the number of spaces in the string.

# def count_space(str):
#     count = 0
#     for ch in str:
#         if ch==' ':
#             count += 1
#     return count

# str = input("Enter your string: ")
# print("Total no. of spaces in string is {}".format(count_space(str)))


# Question 8 : Write a program to check whether 2 lists share no common elements

# list1 =[1,2,3] 
# list2 =[3,4]

# set1 = set(list1)
# set2 = set(list2)

# result = set1.intersection(set2)

# if len(result) == 0:
#     print("No common elements")
# else:
#     print(f"It has common elements {result}")


# Question 9 : print all elements that appear more than once in a list

# list = [1, 2, 3, 2, 4, 5, 1, 6, 2,3,6,4,5]

# seen = set()
# duplicates = set()

# for val in list:
#     if val in seen:
#         duplicates.add(val)
#     else:
#         seen.add(val)
    
# print(duplicates)


# Question 10:

str = input("Enter your string: ")

str_set = set()

for ch in str:
    str_set.add(ch)

print(len(str_set))
