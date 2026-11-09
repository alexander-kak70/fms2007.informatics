# Задача: На вход подаётся натуральное число n < 100. Это число помещается в список. Каждое следующее
# число списка образуется прибавлением к предыдущему числу его максимальной цифры. Создайте
# такой список, чтобы последнее число не превосходило 33000.
# Пример: если n = 3, первые числа списка: [3, 6, 12, 14, 18, 26, 32, 35, 40, 44, ...].

# поиск максимальной цифры в числе
def get_max_digit(number):
    result = 0
    while number > 0:
        r = number % 10
        number = number // 10
        result = max(result, r)

    return result


# вычисление следующего элемента в списке
def calculate_new_list_element(numbers):
    previous_value = get_last_element(numbers)
    new_value = previous_value + get_max_digit(previous_value)
    return new_value


def create_list(n):
    if not 1 <= n < 100:
        raise ValueError("Введите натуральное число от 1 до 99")

    numbers = [n]
    while get_last_element(numbers) < 33000:
        numbers.append(calculate_new_list_element(numbers))
    return numbers


def get_last_element(numbers):
    return numbers[-1]


def main_program():
    try:
        n = int(input("Введите натуральное число от 1 до 99: "))
        numbers = create_list(n)
    except ValueError:
        print("Неверно набран номер!")
        main_program()
    else:
        print(numbers)


if __name__ == '__main__':
    main_program()
