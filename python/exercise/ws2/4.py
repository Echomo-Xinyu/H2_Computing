# num string converter

num = {"1": "one", 
        "2": "two", 
        "3": "three", 
        "4": "four", 
        "5": "five", 
        "6": "six", 
        "7": "seven", 
        "8": "eight", 
        "9": "nine", 
        "0": "zero"}

num1 = input("Please input a number: ")
for i in num1:
    print(num[i], end=' ')

print()
def output(str):
    if len(str)!=0:
        a = str[0]
        print(num[a], end=' ')
        output(str[1:])
    else:
        return

output("3214")