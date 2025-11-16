
# num = input()
# while num != "Quit":
#     n = int(num)
#     if(n>0):
#         print("Positive")
#     elif(n<0):
#         print("Negative")
#     else:
#         print("Zero")
#     num = input()


def calculator(a,b,opr):
    if(opr=='+'):
        return a+b
    elif(opr=='-'):
        return a-b
    elif(opr=='*'):
        return a*b
    elif(opr=='/'):
        return a/b

# print(calculator(10,5,'*'))

def is_prime(num):
    if num < 2 :
        return False
    if num == 2 :
        return True
    for i in range(3,num):
        if(num % i == 0):
            return False
    return True

# print(is_prime(17))

def guess_game():
    secret = 12
    num = int(input("Enter your guess: "))
    while True :
        if(num==secret):
            print("Correct!")
            break
        elif(num>secret):
            print("Too high")
        elif(num<secret):
            print("Too Low")
        num = int(input("Enter your guess: "))

guess_game()
