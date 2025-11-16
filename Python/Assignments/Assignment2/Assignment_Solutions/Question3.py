num = int(input("Enter num: "))
      

def print_digit(num):
    while num > 0 :
        print(num%10)
        num //= 10

print_digit(num)