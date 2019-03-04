c_cent_num_10c = int(input("Enter the number of 10-cent coins inserted: \n"))
c_cent_num_20c = int(input("Enter the number of 20-cent coins inserted: \n"))
c_cent_num_50c = int(input("Enter the number of 50-cent coins inserted: \n"))
c_cent_num_1d = int(input("Enter the number of 1-dollar coins inserted: \n"))
type_drink = float(input("Please enter either the price of the drink, i.e., 0.8 or 1.2: \n"))

total_inserted = 10 * c_cent_num_10c + 20 * c_cent_num_20c + 50 * c_cent_num_50c + 100 * c_cent_num_1d
print("Total inserted: $" + str(total_inserted) + '\n')
    

money_returned = total_inserted - int(type_drink*100)
# print(total_inserted, type_drink, money_returned)

print("The machine returns a total of $" + str(money_returned) + ", in the form of: \n")
money_type = [100, 50, 20, 10]
number_returned = []
count=0
for i in money_type:
    a = money_returned // i
    
    number_returned.append(a)
    # if i==0.1:
    print(a, i, number_returned[count], money_returned)
    money_returned -= a * i
    count+=1
'''
total_inserted = 0.1 * c_cent_num_10c + 0.2 * c_cent_num_20c + 0.5 * c_cent_num_50c + 1 * c_cent_num_1d
print("Total inserted: $" + str(total_inserted) + '\n')
    

money_returned = total_inserted - type_drink
# print(total_inserted, type_drink, money_returned)

print("The machine returns a total of $" + str(money_returned) + ", in the form of: \n")
money_type = [1, 0.5, 0.5, 0.1]
number_returned = []
count=0
for i in money_type:
    a = money_returned // i
    
    number_returned.append(a)
    # if i==0.1:
    print(a, i, number_returned[count], money_returned)
    money_returned -= a * i
    count+=1

''
Output for above is
3.0 1 3.0 3.8
1.0 0.5 1.0 0.7999999999999998
1.0 0.2 1.0 0.2999999999999998
0.0 0.1 0.0 0.09999999999999981
3 * 1-dollar coin(s)
1 * 50-cent coin(s)
1 * 20-cent coin(s)
0 * 10-cent coin(s)
which is the problem about the accuracy of float
''
'''

print(str(int(number_returned[0])) + " * 1-dollar coin(s)")
print(str(int(number_returned[1])) + " * 50-cent coin(s)")
print(str(int(number_returned[2])) + " * 20-cent coin(s)")
print(str(int(number_returned[3])) + " * 10-cent coin(s)")