import random

lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
specialcase = "!@$%^&*"

length = int(input("Enter length of password: "))
keys = lowercase+uppercase+number+specialcase
password = random.sample(keys,k=length)

print("Password: "+"".join(password))