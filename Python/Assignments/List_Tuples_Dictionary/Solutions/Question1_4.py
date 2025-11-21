# Question1: Check if a string is palindrome or not

# str = input("Enter string: ")



def isPal(str):
    reverse_str = str[::-1]
    if str==reverse_str:
        return True
    return False


# if(isPal(str)):
#     print(f"{str} is a palindrome string.")
# else:
#     print(f"{str} is not a palindrome string.")


# Question 2 : Computer the average of integer in the list

list = [3,5,4,6,9,6]

def compute_avg(list):
    sum = 0
    for val in list:
        sum += val
    return sum/len(list)

# print(f"Average of {list} is : {compute_avg(list)}")


# Question 3 : Input two list and merge it and sort and return to the user

# size1 = int(input("Enter size of list1: "))
# list1 = []
# while size1 > 0 :
#     list1.append(int(input("Enter val of list1: ")))
#     size1 -= 1

# print(list1)

# size2 = int(input("Enter size of list2: "))
# list2 = []
# while size2 > 0 :
#     list2.append(int(input("Enter val of list2: ")))
#     size2 -= 1

# print(list2)

# merged_list = list1 + list2
# merged_list.sort()

# print(merged_list)


# Question 4 : Given a tuple of integer create a separate odd and even tuple

tup = (1,2,3,4,5,6,7,8,9,10)

even = []
odd = []
for val in tup:
    if val%2==0:
        even.append(val)
    else:
        odd.append(val)

even_tup = tuple(even)
odd_tup = tuple(odd)

print(even_tup)
print(odd_tup)



