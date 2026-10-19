numbers = [5, 12, 7, 20, 3]

def count_greater(numbers):
    count = 0

    for number in numbers:
        if number > 10:
            count += 1

    print(count)

count_greater 