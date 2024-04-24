## Solutions
1. We can do this with the `readlines()` function:
```
def num_lines(filename):
    with open(filename) as f:
        return len(f.readlines())
```
2. This is the rare use of the 'a' argument to `open()`:
```
def append_to_file(filename):
    with open(filename, 'a') as f:
        f.write('banana')
```
3. We have to do this in two steps: a read, then a write:
```
def remove_es(filename):
    with open(filename) as f:
        contents = f.read()
    new_contents = contents.replace("e", "")  # replace all e's with nothing
    with open(filename, 'w') as f:
        f.write(new_contents)
```
4. There is almost certainly a cleaner way to do this with the `csv` library, but let's do it manually:
```
def csv_transpose(csvfile):
    with open(csvfile) as f:
        parsed = []
        for line in f.readlines():
            parsed.append(line.strip().split(","))
    # parsed is now a list of lists, where each list is one row of the csv. Let's assume it isn't empty.
    new_data = []
    # Build up each row element by element, by traversing one column of parsed
    for i in range(len(parsed[0]):
        new_row = []
        for row in parsed:
            new_row.append(row[i])
        new_data.append(new_row)
    with open("new_csv.csv", 'w') as f:
        for row in new_data:
            # need a newline at the end to produce a true CSV - otherwise we'd have one nightmarishly long comma-separated line
            f.write(",".join(row) + "\n")
```
5. Left as an exercise due to lack of time :P