def input_sequence_processor():
    count_runtime = 0
    count_type = 0
    count_value = 0

    print("Введіть послідовність цифр (від 0 до 9). Для завершення введіть 'досить'.")

    while True:
        user_input = input("Введіть цифру або слово 'досить': ")

        if user_input.lower() == 'досить':
            break

        try:
            number = float(user_input)

            if number > 9:
                raise RuntimeError("Число більше 9")
            elif number < 0:
                raise TypeError("Число меньше 0")
            elif 0 <= number <= 9 and number % 1 != 0:
                raise ValueError("Введено дійсне значення (не ціле)")
            else:
                pass

        except ValueError:
            count_value += 1
        except RuntimeError:
            count_runtime += 1
        except TypeError:
            count_type += 1
        except Exception:
            pass

    print("\nПідрахунок виключень:")
    print(f"Кількість RuntimeError (число > 9): {count_runtime}")
    print(f"Кількість TypeError (число < 0): {count_type}")
    print(f"Кількість ValueError (не число або дійсне в діапазоні): {count_value}")

input_sequence_processor()
