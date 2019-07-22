handle = open("ENCRYPTED.txt", "r")
i = 0

line_content = []
for line in handle:
    if i==0:
        first_line = line
        # i += 1
    else:
        line_content.append(line)
    i += 1
# print(i)

gb = int(first_line[:2])
# print(gb)

num_line = i - 1
# print(num_line)

# print(i)
base = [0 for i in range(i-1)]

def k2d(s, k):
    mapping = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = 0
    for i in range(len(s)):
        result += mapping.index(s[i]) * k ** (len(s)-1-i)
    return result

# process the base of each line
for index in range(i-1):
    # index_l, index_r = 5*index+2, 5*index+7
    # print(first_line[index_l:index_r])
    base[index] = k2d(first_line[5*index+6], gb)

# for i in range(len(base)):
#     print(base[i])
overall_lines = []
for i in range(num_line):
    current_line = line_content[i].strip()
    # print(current_line)
    current_line_content = []
    number_substring = len(current_line) // 8
    # print(number_substring)
    for j in range(number_substring):
        index_l, index_r = j*8, j*8+8
        if j+1 < number_substring:
            substring = current_line[index_l:index_r]
            # print(substring)
            # print(k2d(substring, base[i]))
            current_line_content.append(k2d(substring, base[i]))
        else:
            # print("j", j)
            # print(base)
            substring = current_line[index_l:]
            # print(k2d(substring, base[i]))
            current_line_content.append(k2d(substring, base[i]))
        # # print(current_line_content)
        # if j==0:
        #     print(current_line_content)
    overall_lines.append(current_line_content)
    for i in range(len(current_line_content)):
        print(chr(current_line_content[i]), end="")
    print()

handle.close()

def d2k(d, k):
    result = ""
    mapping = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while d>0:
        digit = mapping[d%k]
        result = digit+ result
        d = d // k
    return result

def process_string(string, desired_length):
    n = len(string)
    additional_string = ""
    if desired_length>n:
        for i in range(desired_length-n):
            additional_string += "0"
    # print(additional_string+string)
    return additional_string+string

# print(process_string("B", 2))

handle = open("newencode.txt", "w")
handle.write(str(gb))
for i in range(len(base)):
    substring = str(d2k(base[i], gb))
    processed_substring = process_string(substring, 5)
    # print(processed_substring)
    handle.write(processed_substring)
handle.write("\n")

for i in range(len(base)):
    current_line_content = overall_lines[i]
    for j in range(len(current_line_content)):
        current_number = current_line_content[j]
        substring = d2k(current_number, base[i])
        processed_substring = process_string(substring, 8)
        # print(processed_substring)
        handle.write(processed_substring)
    handle.write("\n")
    # print(current_line_content)

