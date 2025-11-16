n1 = int(input("Enter num1: "))
n2 = int(input("Enter num2: "))



def print_even(n1,n2):
    print("All even numbers between", n1," and", n2)
    for i in range(n1,n2+1):
        if (i%2==0):
            print(i)


print_even(n1,n2)
