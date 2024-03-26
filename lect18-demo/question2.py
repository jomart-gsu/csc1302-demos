def question2(s):
    # A,B,C -> [A, B, C]
    words = s.split(",")

    # [A, B, C] -> A B C
    return " ".join(words)
