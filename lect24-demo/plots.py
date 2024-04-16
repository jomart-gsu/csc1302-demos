import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# line: coffee vs. social function
x = pd.Series([0,1,2,3,4])
y = pd.Series([5,8,7,3,1])
plt.subplot(2,1,2)
plt.plot(x,y,'g-')
plt.xlabel('Number of cups of coffee')
plt.ylabel('Ability to function in society')


# bar: swear jar
x = pd.Series(["Code not working", "Volleyball", "Stubbed Toe"])
y = pd.Series([2, 20, 3])
plt.subplot(2,1,1)
plt.bar(x,y)
plt.xlabel('Reason')
plt.ylabel('Count')
plt.title("Number of times I've shouted profanity recently, by cause")


# scatter: exam 1 scores vs. exam 2 scores (scatter)
# x = pd.Series([60, 75, 80, 85, 30, 50, 93])
# y = pd.Series([70, 85, 82, 80, 55, 45, 90])
# plt.scatter(x,y)
# plt.xlabel('Exam 1 Score')
# plt.ylabel('Exam 2 Score')
# plt.xlim([0, 100])
# plt.ylim([0, 100])

# pie chart: amount of pie chart taken up
# labels = ['Blue', 'Orange', 'Green']
# sizes = [30, 40, 20]
# plt.pie(sizes, labels=labels)
# plt.title('Percentage of Pie Chart Occupied per Color')

plt.tight_layout()
plt.show()

