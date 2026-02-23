import random
secret = random.randint(1, 100)

print("Guess a number between 1 and 100.")

while True:
    guess = int(input("make your guess: "))
    if guess < secret:
        print ("too low")
    elif guess > secret:
        print ("too high")
    else:
        print ("you got it")
        break
