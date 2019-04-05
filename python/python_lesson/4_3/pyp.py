# Task 4.1
# the function swaps the ath and bth row from the 2D array arr
def row_swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]
    return arr


# the function swaps the ath and bth column from the 2D array arr
def column_swap(arr, a, b):
    for lis in range(len(arr)):
        arr[lis][a], arr[lis][b] = arr[lis][b], arr[lis][a]
    return arr


# Task 4.2
# the function rotate the given 2D array arr
# for n times clockwise direction
def rotate(arr, n=1):
    # for i in range(n):
    #     arr[0][0], arr[0][2], arr[2][0], arr[2][2] = arr[2][0], arr[0][0], arr[2][2], arr[0][2]
    #     arr[0][1], arr[1][0], arr[1][2], arr[2][1] = arr[1][0], arr[2][1], arr[0][1], arr[1][2]
    length = len(arr)
    half_length = length // 2
    # how many times to carry out the rotation
    for i in range(n):
        for j in range(0, half_length):
            for k in range(0, half_length):
                arr[j][k], arr[j][length - k - 1], arr[length - j - 1][
                    length - k - 1], arr[length - j - 1][k] = arr[
                        length - j - 1][k], arr[j][k], arr[j][
                            length - k - 1], arr[length - j - 1][length - k -
                                                                 1]
        if length % 2 == 1:
            for j in range(half_length):
                arr[half_length][j], arr[j][half_length], arr[half_length][
                    length - j - 1], arr[length - j - 1][half_length] = arr[
                        length - j - 1][half_length], arr[half_length][j], arr[
                            j][half_length], arr[half_length][length - j - 1]
    return arr


# Task 4.3
arr1 = [[1, 0, 1], [1, 1, 0], [0, 1, 1]]
arr2 = [[0, 0, 0, 1], [0, 0, 1, 0], [1, 1, 0, 0], [0, 0, 0, 0]]
arr3 = [[1, 0, 0, 1, 1], [0, 0, 1, 0, 1], [1, 1, 1, 1, 1], [0, 0, 1, 1, 0],
        [1, 1, 0, 0, 1]]


def printArr(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=" ")
        print()


printArr(row_swap(arr1, 1, 2))
printArr(column_swap(arr2, 3, 1))
printArr(rotate(arr1, 1))
