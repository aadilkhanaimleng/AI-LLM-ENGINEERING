#counter=kitna
#maan lo hame pata krne hai 1-10 me kitne even number hai
count = 0

for i in range(1, 11):
    if i % 2 == 0:
        count += 1


print(count)
  