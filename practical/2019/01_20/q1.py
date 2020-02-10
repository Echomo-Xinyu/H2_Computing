# q1
def hex2Str(data):
    mapping = "0123456789abcdef"
    result = 0
    for i in range(len(data)):
        # print(data[i])
        result += mapping.index(data[i]) * (16 ** (len(data) - i - 1))
    # print(result)
    return chr(result)

# hex2Str("41")

# q2
ITEMS_DATA = []
handle = open("ITEMS.TXT", 'r')
for line in handle:
    raw_data = line.strip().split(' ')
    processed_data = []
    current_line = ""
    for i in range(len(raw_data)):
        current_line += hex2Str(raw_data[i])
        # processed_data.append(hex2Str(raw_data[i]))
    ITEMS_DATA.append(current_line.split(",")[1])
handle.close()

# handle = open("ITEMS2.TXT", "w")
# for i in range(len(ITEMS_DATA)):
#     c_line = ITEMS_DATA[i]
#     # assert c_line == 2
#     for j in range(len(c_line)):
#         # print(c_line[j], end="")
#         handle.write(c_line[j])
#     handle.write("\n")
#     # print()
# handle.close()

# q3
def mergeSort(arr):
    length = len(arr)
    if length > 1:
        mid = length // 2
        left = arr[:mid].copy()
        right = arr[:mid].copy()
        left = mergeSort(left)
        right = mergeSort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j+= 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            k += 1
            i += 1
        while j < len(right):
            arr[j] = right[j]
            k += 1
            j += 1
    return arr

# q4
CHATACTER_DATA, processed_data = [], []
handle = open("CHARACTERS.TXT", "r")
for line in handle:
    current_line, item_id, process_line = [], [], ""
    raw = line.strip().split(" ")
    for i in range(len(raw)):
        new_char = hex2Str(raw[i])
        process_line += new_char
    processed_data.append(process_line)
# for i in range(len(processed_data)):
#     print(processed_data[i])
# print("\n\n\n\n\n")

for i in range(0, len(processed_data), 2):
    current_line = []
    item_id = []
    line1, line2 = processed_data[i], processed_data[i+1]
    raw1, raw2 = line1.strip().split(","), line2.strip().split(",")
    for j in range(len(raw1)):
        current_line.append(raw1[j])
    for j in range(len(raw2)):
        item_id.append(raw2[j])
    current_line.append(item_id)
    CHATACTER_DATA.append(current_line)
handle.close()
# for i in range(len(CHATACTER_DATA)):
#     print(i)
#     print(CHATACTER_DATA[i])

# q5
request_name = input("Enter name:")
def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i][0] == target:
            return i
    return -1
index = linearSearch(CHATACTER_DATA, request_name)
# if index == -1:
if index != -1:
    c = CHATACTER_DATA[index]
    print("{0}({1}), {2}/{3}/{4}/{5}".format(c[0], c[1], c[2], c[3], c[4], c[5]))
    item_list = []
    for i in range(len(c[6])):
        if i + 1 == len(c[6]):
            print(ITEMS_DATA[int(c[6][i])])
            break
        print(ITEMS_DATA[int(c[6][i])], end=",")
else:
    print("Character not found")