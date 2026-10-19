numbers = [2, 4, 6, 8]

def calculate_square_sum(numbers):
    total = 0

    for number in numbers:
        total += number ** 2

    return total


result = calculate_square_sum(numbers)

print(result)

