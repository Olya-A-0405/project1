from pathlib import Path
def total_salary(path):
    try:
        with open(path, "r") as file:
            salaries = [int(line.split(",")[1]) for line in file if line.strip()]

        total = sum(salaries)
        average = int(total / len(salaries)) if salaries else 0
        return total, average

    except FileNotFoundError:
        print("Помилка: Файл не знайдено.")
        return None
    except ValueError:
        print("Помилка: Неправильний формат даних у файлі.")
        return None

path_to_file = "4task1.txt"
total, average = total_salary(path_to_file)
if total is not None:
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
