import random
upper ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = upper.lower()
numbers = "0123456789"
symbols = "!@#$%^&*().,?}:>;<{;'"
Password_Length=int(input("Enter the length of ur Password which you want: "))

final_outcome= upper+lower+numbers+symbols
password = "".join(random.sample(final_outcome,Password_Length))

print("Your Password is",password)


