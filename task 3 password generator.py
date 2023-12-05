import random
import string
length = int(input("Enter the length of the Password: "))

characters = string.ascii_letters + string.digits + string.punctuation

Pass = " "
for i in range(length):
  Pass=Pass+random.choice(characters)

print("Your Password is:", Pass)
