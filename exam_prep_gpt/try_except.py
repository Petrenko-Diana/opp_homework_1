# ############Запросити у користувача число, обробити помилки: введено не число, ділення на нуль
def deviser(n):
    result = 10/n
    return result
try:
    print(deviser(0))
except ValueError:
    print("Not a number")
except ZeroDivisionError:
    print("Division by 0")

# #########################Написати програму калькулятор, яка зчитує два числа, зчитує операції + - * /, обчислює результат, обробляє всі помилки виводу
def calculus(a, b, oper):
    if oper == "+":
        result = a + b
    elif oper == "-":
        result = a - b
    elif oper == "*":
        result = a * b
    elif oper == "/":
        result = a / b
    else:
        print("Unknown operation")
    return result

try:
    print(calculus(27, 9, "+"))
except ZeroDivisionError:
    print("division by zero")
except NameError:
    print("Name is not defined")
except ValueError:
    print("Not a number")


####################### кількість студентів n, для кожного студ вводить ім'я, вводить к-сть оцінок, оцінки.
#####Зберігає дані в словнику: ключ - ім'я, значення - список оцінок. Використовує функцію, яка приймає список оцінок, повертає середній бал
#####Обробляє помилки вводу: введено не число, кількість студентів або оцінок <= 0. Виводить середній бал кожного студента, ім'я студента з найвищим середнім балом.
try:
    n = int(input("Ведіть кількість студентів"))
    if n <= 0:
        raise ValueError

    journal = {}
    for i in range(n):
        name = input("Введіть ім'я студента")
        amount = int(input("Введіть кількість оцінок"))
        if amount <= 0:
            raise ValueError

        lst_grades = []
        for j in range(amount):
            grade = int(input("Введіть оцінки"))
            lst_grades.append(grade)
        journal[name] = lst_grades
    print(journal)

    def average(grades):
        total = sum(grades)
        return total / len(grades)

    for grades in journal.values():
        print(average(grades))

    best_student = " "
    best_ave = 0
    for name, grades in journal.items():
        ave = average(grades)
        print(name, ":", ave)
        if ave > best_ave:
            best_ave = ave
            best_student = name
    print("Найкращий середній бал у:", best_student)
except ValueError:
    print("Некоректні вхідні дані")


