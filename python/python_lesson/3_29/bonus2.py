# # the function @checkWhetherRect checks whether the array
# # of four coordinbates can form an rectangle
# # by checking whether the mdipoints of diagonals are the same
# # if so whether the lengths of two diagonals are the same
# def checkWhetherRect(arr):
#     (a1, b1), (a2, b2), (a3, b3), (a4, b4) = arr[0], arr[1], arr[2], arr[3]
#     if (a1+a2 == a3+a4) and (b1+b2==b3+b4):
#         length1 = (a2 - a1) ** 2 + (b2 - b1) ** 2
#         length2 = (a3 - a4) ** 2 + (b4 - b3) ** 2
#         return length1 == length2
#     elif (a1+a3 == a2+a4) and (b1+b3 == b2+b4):
#         length1 = (a1 - a3) ** 2 + (b1 - b3) ** 2
#         length2 = (a2 - a4) ** 2 + (b2 - b4) ** 2
#         return length1 == length2
#     elif (a1+a4 == a2+a3) and (b1+b4 == b2+b3):
#         length1 = (a1 - a4) ** 2 + (b1 - b4) ** 2
#         length2 = (a2 - a3) ** 2 + (b2 - b3) ** 2
#         return length1==length2
#     else:
#         return False

# # the function @countRect is to count the number of
# # rectangles formed with the coordinates
# # from the array @arr
# def countRect(arr):
#     count = 0
#     n = len(arr)
#     for i in range(0, n-3):
#         for j in range(i+1, n-2):
#             for k in range(j+1, n-1):
#                 for l in range(k+1, n):
#                     coorCheckArray = [arr[i], arr[j], arr[k], arr[l]]
#                     if checkWhetherRect(coorCheckArray):
#                         count += 1
#     return count

# # coodArr = [(0,1), (1,0), (1,1), (1,2), (2,1), (2,2)]
# coodArr = [(0, 2), (1, 0), (1,4), (2,0)]
# print(countRect(coodArr))