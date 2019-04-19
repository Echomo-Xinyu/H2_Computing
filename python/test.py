# # def f(n, d):
# #     if n==1:
# #         if str(n) == d:
# #             return 1
# #         else:
# #             return 0
# #     str_n = str(n)
# #     count = 0
# #     for i in str_n:
# #         if i==d:
# #             count += 1
# #     return count+f(n-1, d)

# # def f1(n, d):
# #     count = 0
# #     for j in range(1, n+1):
# #         str_n = str(j)
# #         for i in str_n:
# #             if i==d:
# #                 count += 1
# #     return count

# # # n: 
# # def f2(n, d):
# #     str_n = str(n)
# #     len_n = len(str_n)
# #     count = 0
# #     num_d = int(d)
# #     for i in range(len_n):
# #         cur_num = int(str_n[i])
# #         if cur_num < num_d:
# #             if i != 0:
# #                 plus = int(str_n[:i]) * 10 ** (len_n - (i+1))
# #                 # print("a is executed: ")
# #                 # print("plus: ", plus)
# #                 # print("count: ", count)
# #                 count += plus
# #                 # print("count: ", count, '\n\n')
# #             # if i + 1 < len_n:
# #             #     plus = int(str_n[i+1:]) + 1
# #             #     print("b is executed: ")
# #             #     print("plus: ", plus)
# #             #     print("count: ", count)
# #             #     count += plus
# #             #     print("count: ", count, '\n\n')
# #         else:
# #             if cur_num == num_d:
# #                 if i+1<len_n:
# #                     plus = int(str_n[i+1:]) + 1
# #                 else:
# #                     plus = 1
# #                 # print("d is executed: ")
# #                 # print("plus: ", plus)
# #                 # print("count: ", count)
# #                 count += plus
# #                 # print("count: ", count, '\n\n')
# #                 if i != 0:
# #                     pre = int(str_n[:i])
# #                 else:
# #                     pre = 0
# #                 plus = pre * 10 ** (len_n - (i+1))
# #                 # print("c is executed: ")
# #                 # print("plus: ", plus)
# #                 # print("count: ", count)
# #                 count += plus
# #                 # print("count: ", count, '\n\n')
# #             else:
# #                 if i != 0:
# #                     pre = int(str_n[:i]) + 1
# #                 else:
# #                     pre = 1
# #                 plus = pre * 10 ** (len_n - (i+1))
# #                 # print("c is executed: ")
# #                 # print("plus: ", plus)
# #                 # print("count: ", count)
# #                 count += plus
# #                 # print("count: ", count, '\n\n')
# #     if num_d==0:
# #         for i in range(len(str(count))):
# #             count -= 10 ** i
# #     return count

# # print(f1(127930, "4"))
# # print(f2(127930, "4"))

# L = [5, 3, 2, 4, 1]
# # for i in range(len(L)-1):
# #     for j in range(len(L)-i-1):
# #         if L[j] > L[j+1]:
# #             L[j], L[j+1] = L[j+1], L[j]

# # def quickSort(L):
# #     if len(L) < 2:
# #         return L
# #     pivot = L[0]
# #     less, more = [], []
# #     for i in range(1, len(L)):
# #         if L[i] < pivot:
# #             less.append(L[i])
# #         else:
# #             more.append(L[i])
# #     return quickSort(less) + [pivot] + quickSort(more)

# # arr = quickSort(L)

# def qs(L):
#     # if len(L) < 2:
#     #     return L
#     return qs([L[i] for i in range(len(L)) if L[i] < L[0]]) + [L[0]] + qs([L[j] for j in range(len(L)) if L[j] > L[0]]) if len(L) >= 2 else L
# # for i in range(len(arr)):
# #     print(arr[i])

# print(qs(L))

# def selectionSort(L):
#     n = len(L)
#     for i in range(n):
#         index = i
#         for j in range(i+1, n):
#             if L[index] > L[j]:
#                 index = j
#         L[i], L[index] = L[index], L[i]
#     return L

# L = [1, 9, 2, 6, 3, 2, 4, 5, 1]
# print(selectionSort(L))