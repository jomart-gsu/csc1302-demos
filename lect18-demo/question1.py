def question1(arr):
    """
    [
        [1,2,3],     [7,4,1]
        [4,5,6],  -> [8,5,2]
        [7,8,9]      [9,6,3]
    ]
    """
    # get size of the array
    num_rows = len(arr)
    num_cols = len(arr[0])

    # create an empty copy of the array (all zeroes)
    result = []
    for i in range(num_rows):
        row = []
        for j in range(num_cols):
            row.append(0)
        result.append(row)

    for i in range(num_rows):
        for j in range(num_cols):
            result[j][num_rows - i - 1] = arr[i][j]

    return result
