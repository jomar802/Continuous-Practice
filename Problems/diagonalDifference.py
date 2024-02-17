

# Receives a 2d array. Must calculate the diagonal sum of the matrix. 
# Verify that matrix is symmetrical.


def diagonalDifference(arr):
    size_n = len(arr)
    x = 0
    y = 0
    sum = 0
    rx = size_n-1
    ry = 0
    left_to_right = 0
    right_to_left = 0

    for i in range(0,size_n):
        left = arr[x][y]
        right = arr[rx][y]

       
        left_to_right = left + left_to_right
        right_to_left = right + right_to_left

        sum = abs(left_to_right - right_to_left)
        
        x = x + 1
        y = y + 1
        rx = rx - 1

        if(x == size_n):
            break

    return sum



arr = [[1,2,2],[2,1,2],[2,2,1]]


print(diagonalDifference(arr))
