name = input("Enter your name ")
print("Welcome to the quiz " + name)

play = input("Are you ready? ")
while True:
    if play.lower() != "yes":
        break
    print("Let's start")
    score = 0

    question = input("What is the capital city of Nepal? ")
    if question.lower() == "kathmandu":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    question = input("What is the capital city of India? ")
    if question.lower() == "new delhi":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    question = input("What is the capital city of Australia? ")
    if question.lower() == "melbourne":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    question = input("What is the capital city of Germany? ")
    if question.lower() == "berlin":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    question = input("What is the capital city of Japan? ")
    if question.lower() == "tokyo":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    print("You got " + str(score) + " questions correct")
    print("You got " + str(score/5 * 100) + "%")
    play = input("Do you want to play again? ")






