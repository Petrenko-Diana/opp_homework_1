from prep import evaluate_rational_expression
import os


def main():
    input_file = 'input.txt'

    if not os.path.exists(input_file):
        print(f"Помилка: Файл {input_file} не знайдено.")
        return

    with open(input_file, 'r') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line: continue

            try:
                result = evaluate_rational_expression(line)
                print(f"Рядок {line_num}:")
                print(f"  Вираз: {line}")
                print(f"  Результат (дріб): {result}")
                print(f"  Результат (десятковий): {result():.4f}")
            except Exception as e:
                print(f"Помилка в рядку {line_num}: {e}")


if __name__ == "__main__":
    main()
