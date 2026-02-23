import random

print ("Вас вітає математичний тренажер! Введіть 'стоп' щоб вийти.")
input().split()

while True:
    a = random.randint(1,100)
    b = random.randint(1,100)
    op = random.choice(['+','-','*','/'])


    if op == '+':
        correct = a + b
    elif op == '-':
        correct = a - b
    elif op == '*':
        correct = a * b
    else:
        correct = a / b
        print(f"{(a/b):.1f}")

    answer = input(f" Скільк буде {a} {op} {b}")

    if answer.lower() == "стоп":
        print("Game is over")
        break
    if float(answer) == correct:
        print("Correct")
    else:
        print("Incorrect, the answer is:", {correct} )