fileHandle = open("WORDS.TXT", "r")
# count = 0
max_o = -1
max_string = ""
string = ""
for line in fileHandle:
    # count += 1
    # count %= 2
    # if count == 1:
    #     string = str(line.strip())
    # elif count == 0:
    #     try:
    #         num = int(line.strip())
    #     except:
    #         continue
    #     if num > max_o:
    #         max_o  = num
    #         max_string = string
    try:
        num = int(line.strip())
        if num > max_o:
            max_o = num
            max_string = string
    except ValueError:
        string = str(line.strip())
    except:
        print("Wrong input. Please check again")
        break
print(max_o, max_string)
    
