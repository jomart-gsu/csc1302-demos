arr = [
    [2,3,4,5,6],
    [4,5,3,4,5,3],
    [1,4,3,5],
]

def find_one(matrix):
    i = 0
    for row in matrix:
        j = 0
        for num in row:
            if num == 1:
                return i, j

            j += 1
        i += 1

print(find_one(arr))










def f():
    raise TypeError

def g():
    try:
        f()
    except TypeError:
        print("f() didn't work out")
g()




