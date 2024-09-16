import threading
import random
import math


def generate_numbers(file_path):
    with open(file_path, 'w') as file:
        for _ in range(100):
            num = random.randint(1, 1000)
            file.write(str(num) + '\n')
    print("Файл успешно заполнен случайными числами")


def find_prime_numbers(input_file, output_file):
    prime_numbers = []
    with open(input_file, 'r') as file:
        for line in file:
            num = int(line)
            if num > 1:
                is_prime = True
                for i in range(2, int(math.sqrt(num)) + 1):
                    if num % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    prime_numbers.append(num)

    with open(output_file, 'w') as file:
        for prime_num in prime_numbers:
            file.write(str(prime_num) + '\n')
    print("Найдены простые числа и записаны в файл")


def calculate_factorials(input_file, output_file):
    factorials = []
    with open(input_file, 'r') as file:
        for line in file:
            num = int(line)
            factorial = math.factorial(num)
            factorials.append(factorial)

    with open(output_file, 'w') as file:
        for factorial in factorials:
            file.write(str(factorial) + '\n')
    print("Вычислены факториалы чисел и записаны в файл")


if __name__ == '__main__':
    file_path = input("Введите путь к файлу: ")

    input_file = "input.txt"
    output_prime_file = "prime_numbers.txt"
    output_factorial_file = "factorials.txt"

    generate_thread = threading.Thread(target=generate_numbers, args=(file_path,))
    prime_thread = threading.Thread(target=find_prime_numbers, args=(file_path, output_prime_file))
    factorial_thread = threading.Thread(target=calculate_factorials, args=(file_path, output_factorial_file))

    generate_thread.start()
    generate_thread.join()

    prime_thread.start()
    factorial_thread.start()

    prime_thread.join()
    factorial_thread.join()

    print("Статистика выполненных операций:")
    print("Простые числа записаны в файл:", output_prime_file)
    print("Факториалы чисел записаны в файл:", output_factorial_file)