def calculate_next_line(prev):
    next = []
    curr_number = prev[0]
    count = 0
    i = 0
    while i < len(prev):
        # keep iterating until we find a different number
        if prev[i] == curr_number:
            count += 1
        else:
            # if the number changes, append two things to the list
            # 1) how many of the previous number we saw in a row 2) that number
            next.append(count)
            next.append(curr_number)
            curr_number = prev[i]
            count = 1  # need to reset to 1 because prev[i] is the first instance of curr_number, and i is going to increase from here
        i += 1

    return next
def puzzle(n):
    prev = [1]
    # Basic idea: take the previous line, compute the next line from that, repeat with that new line
    # Repeat until done
    for i in range(n):
        next = calculate_next_line(prev)  # We'll use a separate function call to make the overall logic clearer
        print(next)
        prev = next

puzzle(10)