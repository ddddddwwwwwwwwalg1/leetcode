def func(nums):

    a = [[0 for _ in range(10)] for _ in range(9)]
    b = [[0 for _ in range(10)] for _ in range(9)]
    c = [[[0 for _ in range(10)] for _ in range(3)] for _ in range(3)]

    for i in range(0, 9):
        for j in range(0, 9):
            tmp = nums[i][j]
            if a[i][tmp] == 1:
                return False
            if b[j][tmp] == 1:
                return False
            if c[i//3][j//3][tmp] == 1:
                return False
            a[i][tmp] = 1
            b[j][tmp] = 1
            c[i//3][j//3][tmp] = 1

    return True