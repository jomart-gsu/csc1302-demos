# arr = [
#     [2,3,4,5,6],
#     [4,5,3,4,5,3],
#     [1,4,3,5],
# ]
#
# def find_one(matrix):
#     i = 0
#     for row in matrix:
#         j = 0
#         for num in row:
#             if num == 1:
#                 return i, j
#
#             j += 1
#         i += 1
#
# print(find_one(arr))
#
#
#
#
#
#
#
#
#
#
# def f():
#     raise TypeError
#
# def g():
#     try:
#         f()
#     except TypeError:
#         print("f() didn't work out")
# g()




def calculate_percents():
    while True:
        try:
            x = int(input("Enter a number: "))
            y = int(input("Enter another number: "))
        except ValueError:
            print("Input should be a number")
            continue

        try:
            pct = x / y * 100
        except ZeroDivisionError:
            print("Second number must be nonzero")
            continue

        print(f"{x} is {pct} percent of {y}")



calculate_percents()


