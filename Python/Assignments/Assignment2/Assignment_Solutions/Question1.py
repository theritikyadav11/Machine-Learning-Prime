salary = int(input("Enter your salary: "))

if(salary < 30000) :
    print("Tax: 5%")
elif(salary >= 30000 and salary < 70000):
    print("Tax: 15%")
else:
    print("Tax: 25%")