# Task 2.1
def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j]["age"] > array[j+1]["age"]:
                array[j], array[j+1] = array[j+1], array[j]
            elif array[j]["age"] == array[j+1]["age"]:
                if array[j]["name"] > array[j+1]["name"]:
                    array[j], array[j+1] = array[j+1], array[j]
    return array

arr = [{"name":"H", "age":34},
      {"name":"L", "age":21},
      {"name":"A", "age":21},
      {"name":"M", "age":64}]

#for i in range(4):
#    print(bubbleSort(arr)[i]["name"], bubbleSort(arr)[i]["age"])

# Task 2.2
age_range = ["<10", "[10-19]", "[20-29]", "[30-39]", "[40-49]",
             "[50-59]", "[60-69]", ">=70"]
age_range_count = [0 for i in range(8)]
for i in range(len(arr)):
    age = arr[i]["age"]
    if age >= 70:
        age_range_count[8] += 1
    else:
        for j in range(7):
            if age < (j+1)*10:
                age_range_count[j] += 1
                break

for i in range(8):
    print("{0:7}:{1:1}".format(age_range[i], age_range_count[i]))
