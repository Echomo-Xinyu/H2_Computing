handler = open("PERFECT_SQUARES.TXT", "a")
input_n = int(input("Please input a number n: \n"))
print()
input_m = int(input("Please input a number m: \n"))

for i in range(input_n+1, input_m+1):
    num = i ** 2
    handler.write(str(num) + '\n')

handler.close()