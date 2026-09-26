def sum_digits(number):
    total = 0

    while number > 0:
        total = total + number % 10
        number = number // 10

    return total


ans = []

total = 0

for i in range(1, 16):
    total = total + i

ans.append(total)

while ans[-1] > 0:
    current = ans[-1]
    digits_sum = sum_digits(current)
    next_number = current - digits_sum
    ans.append(next_number)


print("╔════════════════════════════════╗")
print("║        РЕЗУЛЬТАТ ЗАДАЧИ        ║")
print("╚════════════════════════════════╝")

print()
print(" Последовательность:")
print(" → ".join(map(str, ans)))

print()
print(" Количество чисел:", len(ans))
print(" Конечное число:", ans[-1])