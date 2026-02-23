import os


def process_files_from_list(content_filename="content.txt"):
    total_sum = 0
    files_processed = 0

    try:
        with open(content_filename, 'r', encoding='utf-8') as content_file:
            filenames = content_file.readlines()
    except FileNotFoundError:
        print(f"Помилка: Файл '{content_filename}' не знайдено за вказаним розташуванням.")
        return
    except IOError as e:
        print(f"Помилка: Файл '{content_filename}' недоступний для читання. Деталі: {e}")
        return

    for filename_line in filenames:
        filename = filename_line.strip()
        if not filename:
            continue

        file_sum = 0
        file_valid_numbers = 0

        try:
            with open(filename, 'r', encoding='utf-8') as data_file:
                content = data_file.read().split()
                for item in content:
                    try:
                        number = float(item)
                        file_sum += number
                        file_valid_numbers += 1
                    except ValueError:
                        print(f"  [Попередження у файлі '{filename}']: Пропущено нечислове значення '{item}'.")

                if file_valid_numbers > 0:
                    print(f"Успішно опрацьовано файл '{filename}'. Сума чисел: {file_sum:.2f}")
                    total_sum += file_sum
                    files_processed += 1
                else:
                    print(f"Файл '{filename}' не містив дійсних чисел або був порожнім.")

        except FileNotFoundError:
            print(f"Помилка: Файл даних '{filename}' не існує або не знайдено.")
        except IOError as e:
            print(f"Помилка читання файлу даних '{filename}'. Деталі: {e}")


    if files_processed > 0:
        print(f"Загальна сума з усіх опрацьованих файлів: {total_sum:.2f}")
    else:
        print("Не вдалося обробити жоден файл зі списку.")




process_files_from_list("content.txt")
