import math

def read_numbers_from_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            numbers = [int(num) for num in content.split() if num.strip()]
            return numbers
    except FileNotFoundError:
        print(f"Помилка: файл '{filename}' не знайдено.")
        return []
    except ValueError:
        print("Помилка: файл містить нечислові дані.")
        return []


def count_even_numbers(data):
    count = 0
    for num in data:
        if num % 2 == 0:
            count += 1
    return count


def count_squares_of_odd_numbers(data):
    count = 0
    for num in data:
        if num >= 0:
            sqrt_num = int(math.isqrt(num))
            if sqrt_num * sqrt_num == num and sqrt_num % 2 != 0:
                count += 1
    return count


def difference_max_even_min_odd(data):
    even_numbers = [num for num in data if num % 2 == 0]
    odd_numbers = [num for num in data if num % 2 != 0]

    if not even_numbers:
        return "Помилка: у файлі немає парних чисел."
    if not odd_numbers:
        return "Помилка: у файлі немає непарних чисел."

    max_even = max(even_numbers)
    min_odd = min(odd_numbers)

    return max_even - min_odd


def length_of_longest_increasing_sequence(data):
    if not data:
        return 0

    max_length = 1
    current_length = 1

    for i in range(1, len(data)):
        if data[i] > data[i - 1]:
            current_length += 1
        else:
            if current_length > max_length:
                max_length = current_length
            current_length = 1

    if current_length > max_length:
        max_length = current_length

    return max_length

FILE_NAME = "input.txt"

data = read_numbers_from_file(FILE_NAME)

if data:
    print(f"Дані успішно завантажено з файлу '{FILE_NAME}':\n{data}\n")

    print(f"a) Кількість парних чисел: {count_even_numbers(data)}")
    print(f"b) Кількість квадратів непарних чисел: {count_squares_of_odd_numbers(data)}")

    diff_result = difference_max_even_min_odd(data)
    print(f"c) Різниця між найбільшим парним і найменшим непарним: {diff_result}")

    print(f"d) Довжина найдовшої зростаючої послідовності: {length_of_longest_increasing_sequence(data)}")
else:
    print("Не вдалося обробити дані з файлу. Переконайтеся, що файл input.txt існує і містить числа.")


