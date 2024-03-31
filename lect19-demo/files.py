
import os
os.path.expanduser("~")
file = open("/Users/johnmartin/Downloads/shakespeare.txt")

content = file.read()
words = content.split()

from collections import Counter
counts = {}
for word in words:
    if word not in counts:
        counts[word] = 0
    counts[word] += 1

counts = Counter(words)

# {"the": 30, "his": 20, "banana": 1}
# [("the", 30), ("his", 20),

word_list = []
for key, value in counts.items():
    word_list.append((value, key))

word_list.sort(reverse=True)
print(word_list[:10])








# import csv
# """
# Assume names.csv looks like
#
#     first_name,last_name
#     John,Cleese
#     Eric,Idle
#
# """
# with open('names.csv', newline='') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row['first_name'], row['last_name'])
#
# """
# ...will print
#     John Cleese
#     Eric Idle
# """




