import math


def format_text_to_file(text_sequence, output_filename, line_length=40):
    clean_text = text_sequence.replace(" ", "")

    formatted_lines = []
    for i in range(0, len(clean_text), line_length):
        line = clean_text[i:i + line_length]
        formatted_lines.append(line)

    try:
        with open(output_filename, 'w', encoding='utf-8') as file:
            for line in formatted_lines:
                file.write(line + '\n')
        print(f"Файл '{output_filename}' успішно створено.")
        print(f"Кількість рядків у файлі: {len(formatted_lines)}")
    except IOError as e:
        print(f"Помилка запису файлу {output_filename}: {e}")


input_text = "jcm nf pflfxf ghj zre z gbvfkf d vbyekjve gjdsljvktyys"

output_file_name = "output_formatted.txt"

format_text_to_file(input_text, output_file_name)
