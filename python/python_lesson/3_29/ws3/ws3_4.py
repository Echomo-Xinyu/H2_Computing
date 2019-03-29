handler = open("prime1000000.txt", "r")
input_n = int(input("Please input an number to check if it's prime: \n"))
data = []
for line in handler:
    data.append(line.strip())
if input_n >= 1000000:
    print("The number is too big")
else:
    whether_prime = False
    for i in data:
        if int(i) == input_n:
            whether_prime = True
            break
    if whether_prime:
        print("input is a prime")
    else:
        print("Input is not")