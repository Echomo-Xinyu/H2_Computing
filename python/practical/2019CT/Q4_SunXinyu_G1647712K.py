# Task 4.1
def h2d(string):
    k = 16
    mapping = "0123456789abcdef"
    result = 0
    for i in range(len(string)):
        result += mapping.index(string[i]) * k ** (len(string)-i)
    return result

# Task 4.2
def d2h(num):
    k = 16
    result_str = ""
    mapping = "0123456789abcdef"
    while num > 0:
        digit = num % k
        result_str = mapping[digit] + result_str
        num = num // k
    return result_str

#print(d2h(17826048))
#print(h2d("110010"))
#print(d2h(16))

# Task 4.3
# this function assumes only take in a 1d array
def calCheckSum(hexa_list):
    final_den_result = 0
    #print(len(hexa_list))
    for i in range(len(hexa_list)):
        final_den_result += h2d(hexa_list[i])
        #print(final_den_result)
    final_den_result = final_den_result%(16*16)
    #print(final_den_result)
    result = d2h(final_den_result)
    if len(result)==0:
        result = "00"
    elif len(result)==1:
        result = "0" + result
    return result

#arr = ["01", "00", "5e", "7f", "ff", "fa", "00", "f4", "8d", "d6", "79", "c5",
        #"08", "00", "45", "00"]

#print(calCheckSum(arr))

# Task 4.4
file_handle_r = open("hex_dump.txt", "r")
data = []
for line in file_handle_r:
    line_data = line.strip().split(",")
    data.append(line_data)
file_handle_r.close()

file_handle_w = open("checksums_SunXinyu_G1647712K.txt", "w")
for i in range(len(data)):
    for j in range(len(data[0])):
        file_handle_w.write(data[i][j]+",")
    file_handle_w.write(calCheckSum(data[i])+"\n")
    #print(calCheckSum(data[i]))

for j in range(len(data[0])):
    current_row = []
    for i in range(len(data)):
        current_row.append(data[i][j])
    
    file_handle_w.write(calCheckSum(current_row))
    if j+1<len(data[0]):
        file_handle_w.write(",")

file_handle_w.close()
        

