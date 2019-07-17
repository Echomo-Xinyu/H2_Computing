# Task 1.1
num_students = int(input("Please enter the number of students:\n"))
marks = [[None for i in range(5)] for j in range(num_students)]

# read in all the input score
print("Please enter in the format as: Name, 10, 10, 10, 10")
for i in range(num_students):
    while True:
        try:
            input_content = input().split(",")
            if len(input_content) == 5:
                Name = input_content[0]
                English, MT = int(input_content[1]), int(input_content[2])
                Math, Science = int(input_content[3]), int(input_content[4])
                break
            else:
                print("Invalid marks entered, please enter again.")
                continue
        except:
            print("Invalid marks entered, please enter again.")
            continue
    marks[i][0] = Name
    marks[i][1], marks[i][2] = English, MT
    marks[i][3], marks[i][4] = Math, Science

# round up to the nearest multiple of 5
for i in range(num_students):
    for j in range(1, 5):
        # print(marks[i][j], end=" ")
        if marks[i][j] < 45:
            continue
        elif marks[i][j] % 5 < 3:
            marks[i][j] -= marks[i][j] % 5
        else:
            marks[i][j] += 5 - marks[i][j] % 5
    # print()

# Task 1.2
# calculate the average mark
for i in range(num_students):
    Name = marks[i][0]
    sum_score, num_subjects = 0, 4
    for j in range(1, 5):
        sum_score += marks[i][j]
    ave_score = sum_score / num_subjects
    if ave_score % 1 >= 0.5:
        ave_score = ave_score // 1 + 1
    else:
        ave_score = ave_score // 1
    print("Average mark for " + Name + " is " + str(int(ave_score)))

# Task 1.3
sub_list = ["English", "MT", "Math", "Science"]
for i in range(1, 5):
    sub_score_sum = 0
    for j in range(num_students):
        sub_score_sum += marks[j][i]
    sub_ave = sub_score_sum / num_students
    if sub_ave % 1 >= 0.5:
        sub_ave = sub_ave // 1 + 1
    else:
        sub_ave = sub_ave // 1
    print("Average mark for " + sub_list[i - 1] + " is " + str(int(sub_ave)))

# Task 1.4
for i in range(1, 5):
    highest, lowest = 0, 100
    highest_student, lowest_student = "", ""
    for j in range(num_students):
        if marks[j][i] > highest:
            highest = marks[j][i]
            highest_student = marks[j][0]
        if marks[j][i] < lowest:
            lowest = marks[j][i]
            lowest_student = marks[j][0]
        else:
            continue
    print(sub_list[i - 1] + "(Highest, Lowest): " + highest_student + ", " +
          lowest_student)
