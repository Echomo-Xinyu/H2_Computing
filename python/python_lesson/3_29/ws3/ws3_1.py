handler = open("PERFECT_SQUARES.TXT", "w")
input_n = int(input("Please input number n: \n"))
for i in range(1, input_n+1):
    num = i ** 2
    handler.write(str(num) + '\n')

handler.close()