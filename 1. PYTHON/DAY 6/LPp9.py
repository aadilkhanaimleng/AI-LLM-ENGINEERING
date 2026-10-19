numbers = [10, 15, 20, 25, 30]

def sum_even(numbers):
    total = 0

    for number in numbers:
        if number % 2 == 0:
            total += number

    return total


result = sum_even(numbers)

print(result)