"""
This is the code I used to generate the CSV. It's a little sloppy but it gets the job done.
"""
from random import choices
import numpy as np
import pandas as pd

opponentIDs = []
results = []
accuracies = []


wl = ["win", "loss"]
# assume no cheating for first 450 games, then sprinkle in 300 sus games
accuracies = np.append(np.random.normal(75, 10, size=450), np.random.normal(90,3,size=300))
results = choices(wl, [0.6, 0.4], k=450) + choices(wl, [0.8, 0.2], k=300)
opponents = np.random.randint(10000000, 99999999, size=750)
months = np.append(np.random.randint(1, 12, size=450),np.random.randint(1,4,size=300))
years = np.append(np.random.randint(2021, 2023, size=450), np.random.randint(2023, 2024, size=300))


assert len(accuracies) == len(results) == len(opponents) == len(months) == len(years)

# compile stats into a dataframe, then write to CSV
df = pd.DataFrame({
    "year": years,
    "month": months,
    "opponent": opponents,
    "result": results,
    "accuracy": accuracies
})
df.to_csv("record.csv")

