positive = 0
negative = 0
zero = 0

for i in [12, -5, 0, 18, -2, 7, 0, 21, -9, 4]:

    if i > 0:
        positive += 1

    if i < 0:
        negative += 1

    if i == 0:
        zero += 1

print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)

