import math

def calculate_z(m, n):
    """Обчислення значення z = (sqrt(m) - sqrt(n)) / m"""
    try:
        if m > 0 and n > 0:
            z = (math.sqrt(m) - math.sqrt(n)) / m
            return z
        else:
            return "Числа m та n повинні бути додатними!"
    except ZeroDivisionError:
        return "Помилка: ділення на нуль!"

def is_perfect_number(num):
    """Перевірка, чи є число досконалим"""
    if num <= 0:
        return False
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return divisors_sum == num

def main():
    """Основна функція програми"""
    try:
        # Введення чисел m та n
        m = float(input("Введіть число m (додатнє): "))
        n = int(input("Введіть число n (натуральне): "))

        # 1. Обчислення z
        z_result = calculate_z(m, n)
        print(f"Результат обчислення z: {z_result}")

        # 2. Перевірка на досконале число
        if is_perfect_number(n):
            print(f"Число {n} є досконалим.")
        else:
            print(f"Число {n} не є досконалим.")
    except ValueError:
        print("Помилка: введіть коректні числові значення!")

# Запуск програми
main()
