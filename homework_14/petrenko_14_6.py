import math


def get_list_from_user():
    user_input = input("Введіть числа через пробіл: ")
    numbers = [int(num) for num in user_input.strip().split() if num.strip()]
    return numbers


def count_elements(input_list):
    count = 0
    try:
        while True:
            input_list[count]
            count += 1
    except IndexError:
        pass
    return count


def sum_elements(input_list):
    total = 0
    i = 0
    try:
        while True:
            total += input_list[i]
            i += 1
    except IndexError:
        pass
    return total


def max_ratio(input_list):
    max_val = -float('inf')
    i = 0
    while i < count_elements(input_list):
        j = 0
        while j < count_elements(input_list):
            if i != j and input_list[j] != 0:
                ratio = input_list[i] / input_list[j]
                if ratio > max_val:
                    max_val = ratio
            j += 1
        i += 1
    return max_val


user_numbers = get_list_from_user()

if count_elements(user_numbers) < 2:
    print("Помилка: потрібно щонайменше два числа в списку.")
else:
    count = count_elements(user_numbers)
    total_sum = sum_elements(user_numbers)
    max_ratio_val = max_ratio(user_numbers)

    print(f"Кількість елементів: {count}")
    print(f"Сума елементів: {total_sum}")
    print(f"Значення найбільшої частки: {max_ratio_val}")

