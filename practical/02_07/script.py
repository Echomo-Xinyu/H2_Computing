# -*- coding: UTF-8 -*-

# this script is to implemenet something interesting


# qn1: convert an input integer to its 2s complement in binary format
def comp2(integer):
    # print(integer)
    n = integer
    try:
        if int(integer) not in range(-128, 128):
            raise Exception
    except:
        print("Please check the value and type of the input")
        return
    if n < 0:
        magn = -1
    else:
        magn = 1
    n_abs = abs(n)
    n_b = bin(n_abs)[2:]
    # print("The binary form is ", n_b)
    if magn == 1:
        n_b = "0" * (7-len(n_b)) + n_b
        return "0" + n_b
    else:
        n_b = bin(int(n_b, 2) - int("1", 2))[2:]
        n_b = "0" * (7-len(n_b)) + n_b
        new_str = ""
        for j in range(len(n_b)):
            if n_b[j] == "0":
                new_str = new_str + "1"
            else:
                new_str = new_str + "0"
        # print("1", new_str)
        result = "1" + new_str
        result = result[-8:]
        # print(result)
        return result

# print(comp2(-135))
# for i in range(-128,128):
#     print(f"{i:>4}:{comp2(i)}")


# qn2: convery 2s compliment to denary value
def toDec(str):
    mag = -1 if str[0] == "1" else 0
    if mag == 0:
        return int(str[1:], 2)
    else:
        val = int(str[1:], 2)
        acl_val = 128-val
        return -1 * acl_val

# print(toDec("10000000")) # -128
# print(toDec("11110011")) # -13

# qn3: encode the emoji characters using the UTF-8 encoding scheme
# write the emoji to file and read again to output
# replace '+' with 000 from https://www.geeksforgeeks.org/python-program-to-print-emojis/
# \U: 4 byte; \u: 2 byte
emoji_list = ["\U0001F64A", "\U0001f649", "\U0001f648", "\U0001f921"]
# emoji_list = ["🤡", "🙈", "🙉", "🙊"]
# b'\xf0\x9f\x99\x88'
handle = open("emoji.txt", "w", encoding="utf-8")
for _, cha in enumerate(emoji_list):
    handle.write(cha)
handle.close()

f = open('emoji.txt', 'r', encoding='utf-8')
text = f.read()
for i in range(len(text)):
    print(text[i], end=" ")
print()

# qn4: 
# calculate the number of hours that has elapsed since your are born.
# and the number of minutes left before you sit for your A Level Computing practical paper on 2 Oct 2020.
from datetime import date, datetime
birth = date(2001, 9, 5)
today = date.today()
print((today - birth).days * 24)

today = datetime.now()
exam_time = datetime(2020, 10, 2, 8, 0, 0)
day, sec = (exam_time-today).days, (exam_time-today).seconds
print(day*24*60 + sec // 60)