def gcd(number_1: int, number_2: int) -> int: #знаходить найбільший спільний дільник (НСД) двох чисел
    while number_2:
        temp = number_2
        number_2 = number_1 % number_2
        number_1 = temp
    return number_1


result = gcd(48, 18)
print("result: ", result)


def fibonacci(number: int) -> int: #функція реалізує обчислення nn-го числа в ряді Фібоначчі
    if number <= 1:
        return number
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)


result_fib = fibonacci(6)
print("result: ", result_fib)
