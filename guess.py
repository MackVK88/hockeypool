import random
secret_num = random.randint(0,1000)

num = input("enter a number: ")
num = int(num)
chances = 0

while (num != secret_num):
    if (num > secret_num):
        print("too high")
    elif (num < secret_num):
        print("too low")
    num = int(input("enter a number: "))
    chances = chances + 1

print("you win! " + "only" + str(chances) + "tries")