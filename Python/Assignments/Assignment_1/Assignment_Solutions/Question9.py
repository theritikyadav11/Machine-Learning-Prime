p = input("Enter principal amount: ")
r = input("Enter the rate %: ")
t = input("Enter your time: ")

float_p = float(p)
float_r = float(r)
float_t = float(t)

si = float_p * float_r * float_t / 100

print("Simple Interest is: ", si)