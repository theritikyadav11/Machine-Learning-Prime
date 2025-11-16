# num = int(input("Enter num: "))


def print_count(num):
    count = 0
    while num > 0 :
        count += 1
        num //= 10
    
    return count

# print(print_count(num))

def digit_sum(num):
    sum = 0
    while num > 0 :
        sum += num%10
        num //= 10
    return sum

# print(digit_sum(num))

def multiple_3_5():
    for i in range(1,100):
        if(i%3==0 and i%5==0):
            print(i)

multiple_3_5()