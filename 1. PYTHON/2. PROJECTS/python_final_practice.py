marks = [45, 78, 32, 90, 66, 28, 81]

def analyze_marks(marks):
    total = 0
    count = 0

    for mark in marks:
        total += mark

        if mark >= 40:
            count += 1

    return total, count


total, passed = analyze_marks(marks)

print("Total:", total)
print("Students:", len(marks))
print("Passed:", passed)
