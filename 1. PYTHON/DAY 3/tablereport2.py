for i in range(1, 4):
    row_total = 0
    for j in range(1,4):
        result = i * j
        print(result, end=" ")
        row_total = row_total + result

    
    print("| Row Total:", row_total) 