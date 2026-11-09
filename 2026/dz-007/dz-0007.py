# Задача: На вход подаётся натуральное число n < 100. Это число помещается в список. Каждое следующее
# число списка образуется прибавлением к предыдущему числу его максимальной цифры. Создайте
# такой список, чтобы последнее число не превосходило 33000.
# Пример: если n = 3, первые числа списка: [3, 6, 12, 14, 18, 26, 32, 35, 40, 44, ...].

# поиск максимальной цифры в числе
def getMaxDigit(number):
    r = 0  # остаток от деления
    result = 0
    while number > 0:
        r = number % 10
        number = int(number / 10)
        result = max(result, r)

    return result


# вычисление следующего элемента в списке
def calculateNewListElement(list):
    previousValue = getLastElement(list)
    newValue = previousValue + getMaxDigit(previousValue)
    return newValue


def createList(n):
    list = [n]
    while getLastElement(list) < 33000:
        list.append(calculateNewListElement(list))
    return list


def getLastElement(list):
    return list[len(list) - 1]


if __name__ == '__main__':
    n = int(input("Введите число n меньше 100: "))
    if n < 100:
        print(createList(n))
    else:
        print("Введите число меньше 100")
        exit(0)
