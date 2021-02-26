prev, current = 0, 1
sum = 0
while True:
    prev, current = current, prev + current
    if current >= 4000000:
        break
    if current % 2 == 0:
        sum += current
    print(sum)