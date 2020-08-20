# nonlocal variable
max_depth, max_sum = 1, 1
def t():
    nonlocal max_depth
    nonlocal max_sum
    max_depth += 1
    max_sum += 1
    # these will allow value of two variables to be changed along 
    # with operations within the method when being called

# read csv
# it just differs in split with comma
handle = open("a.csv", "r")
for line in handle:
    data_raw = line.strip().split(",")
    # ...
handle.close()

# read json
import json
f = open("a.json", "r")
# this will give a list of dictionary
data = json.load(f)
print(data)