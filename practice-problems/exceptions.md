# Try/Except practice problems
1. What error will this function produce? Fix it so it doesn't raise an exception using `try/except`.
```
def do_something_suspicious():
    l = []
    print(l[2])
```
2. What will the output be if this function is called?
```
def do_something_else():
    try:
        print("Never")
        l = []
        x = 4
        for i in range(3):
            l.append(x / i)
        return len(l)
    except ZeroDivisionError as e:
        print("Gonna")
        raise e
    finally:
        print("Give You Up")       
```
3. Will the above code run without producing an error? Why or why not?
