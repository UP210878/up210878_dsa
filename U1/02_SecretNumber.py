import random

secret = random.randint(0,10)
print(secret)

number = int(input("Enter a number between 0 and 10"))
while number != secret:
    if secret > number:
        print ("Increase the number")
    else:
        print ("Decrease the number")
    number = int(input("Enter a number between 0 and 10"))
print ("Congratulations! You guessed right")