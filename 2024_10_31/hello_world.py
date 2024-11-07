def fibonacci(x: int) -> int:
    if x <= 1:
        return 1

    return fibonacci(x - 1) + fibonacci(x - 2)


print("Hello World")

numbers = []

for i in range(20):
    string_number = str(fibonacci(i))
    numbers.append(string_number)

print(", ".join(numbers))

"""
Output:
Hello World
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765
"""