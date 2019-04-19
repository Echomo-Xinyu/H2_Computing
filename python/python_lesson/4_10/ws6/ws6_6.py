# Task includes:
# 1. Whether perform a search
# 2. ask for input searching category
# 3. ask for the score searching for
# 4. output all the names that statisfy the search criteria
# this works under the assumption of the "DATA.TXT" provided with certain format

handle = open("DATA.txt", "r")
data = []
for line in handle:
    if line != None:
        c_data = line.strip().split(",")
        overall_score = int(c_data[1]*0.1 + c_data[2]*0.15 + c_data[3]*0.25 + c_data[4]*0.5)
        c_data.append(overall_score)
        data.append(c_data)

dict_n = {"test score 1": 1, "test score 2": 2, "test score 3": 3, "test score 4": 4, "overall score": 5}

while(True):
    whether_execute = input("Do you want to perform a search? Y for yes, N for No.\n").lower()
    if whether_execute == "no" or whether_execute == "n":
        break
    elif (not (whether_execute == "yes" and whether_execute == "y")):
        print("Invalid input. Please type again.")
        continue
    category = input("Please input the category you wanna search:\nOverall score\nTest score 1\nTest score 2\nTest score 3\nTest score 4\n").lower()
    if category != "overall score" and category != "test score 1" and category != "test score 2" and category != "test score 3" and category != "test score 4":
        print("Invalid input for category. Please check once again.")
        continue
    score = input("Please input the score you wish to search for:\n")
    try:
        score = int(score)
    except:
        print("Please check your input type.")
        continue
    if category == "test score 1" or category == "test score 2":
        if score < 0 or score > 50:
            print("Invalid score. PLease chekc again")
            continue
    elif category == "test score 3" or category == "test score 4":
        if score < 0 or score > 100:
            print("Invalid score. Please check agian.")
            continue
    category_index = dict_n[category]
    n = len(data)
    for i in range(n):
        if score == data[i][category_index]:
            print(data[i][0])
    continue