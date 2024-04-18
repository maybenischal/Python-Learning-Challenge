import random

top_of_range = input("Type a number: " )

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type the number greater than 0")
        quit()
else:
    print("Please type a number")
    quit()

random_number = random.randint(0, top_of_range)
guess = 0

while True:
    guess += 1
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please make next guess")
        continue

    if user_guess == random_number:
        print("You made the right guess")
        break
    elif user_guess > random_number:
        print("Your guess is above the number")
    else:
        print("Your guess is below the number")

print("You made right guess in", guess, "attempts.")
