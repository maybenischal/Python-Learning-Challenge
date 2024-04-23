import random
import time

opr = [ "+", "-", "*" ]
max_operand = int(input("Enter the maximum value of operand: "))
min_operand = int(input("Enter the minimum value of operand: "))

total_problems = int(input("How many questions you want to get asked? "))

def get_problems():
    left = random.randint(min_operand,max_operand)
    right = random.randint(min_operand,max_operand)
    operator = random.choice(opr)

    expr = str(left)+ " " + operator + " " + str(right)
    ans = eval(expr)
    return expr, ans

input("Press 'Enter' to start the game. ") 
print("------------------------------")
start_time = time.time()

correct_ans = 0
for i in range(total_problems):
    expr, ans = get_problems()
    while True:
        question = input("Problem #" + str(i+1) + ": " + expr + " = ")
        if question == str(ans):
            print("\x1b[32mCorrect Answer\x1b[0m")
            correct_ans += 1
            break
        else:
            print("\x1b[31mWrong Answer\x1b[0m")
            break
end_time = time.time()
total_time = round(end_time - start_time,2)

print("------------------------------")
print("You answered", correct_ans, "out of", total_problems, "questions correctly.")
print("Nice work! You finished in", total_time, "seconds!")