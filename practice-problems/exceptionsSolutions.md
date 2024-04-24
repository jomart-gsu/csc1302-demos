## Solutions
1. As written, the function will produce an `IndexError`. It can be "fixed" as follows:
```
def do_something_suspicious():
    try:
        l = []
        print(l[2])
    except IndexError:
        print("Slow down there, cowboy")
```
(Note that this isn't a realistic example of how exceptions are useful, since the function deterministically produces an error and probably just shouldn't exist to begin with. Exceptions make more sense to use when handling input from the user.)
2. This code will print
```
Never
Gonna
Give You Up
```
because the first iteration of the `for` loop will cause a `ZeroDivisionError`, which will take us into the `except` clause. Once that's done (but BEFORE it raises the exception), the `finally` clause will kick in and print the last statement.
3. No, because the `except` clause still raises the same exception it caught -- it just prints "Gonna" first.