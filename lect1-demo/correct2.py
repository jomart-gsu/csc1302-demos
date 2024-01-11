def calculate_next_line(prev):
    # starting condition: if prev is an empty line, return the first line (just a one)
    if len(prev) == 0:
        return [1]

    next = []
    i = 0
    while i < len(prev):
        j = i
        count = 0

        # we can also use a second nested while loop to avoid that slightly ugly
        # exit condition in correct.py

        # instead of waiting for the number to change and counting how many we saw before then,
        # now we start at the first number and count how many times it happens, then repeat with each
        # successive number, moving left to right
        while j < len(prev) and prev[i] == prev[j]:
            count += 1
            j += 1
        next.append(count) # we don't even technically need count, could just use (j - i)
        next.append(prev[i])
        i = j

    return next
def puzzle(n):
    # this is the second bug! the original code skipped over the first line, which is just "1"
    prev = []
    # Basic idea: take the previous line, compute the next line from that, repeat with that new line
    # Repeat until done
    for i in range(n):
        next = calculate_next_line(prev)  # We'll use a separate function call to make the overall logic clearer
        print(next)
        prev = next

puzzle(10)