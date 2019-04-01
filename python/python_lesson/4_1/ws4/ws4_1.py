numbers = [x for x in range(1000)]
i = 0
while True:
    try:
        print(str(numbers[i]))
    except:
        break
    i += 1