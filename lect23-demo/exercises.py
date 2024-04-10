import pandas as pd


# 1
favs = pd.Series(["Wobbuffet", "Ludicolo", "Meowth", "Jigglypuff", "Gengar"], index=["a", "b", "c", "d", "e"])

# 2
favs.iloc[0]

# 3
favs["b": "d"]

# 4
pokedex = pd.DataFrame(favs, columns=["Pokemon Name"])

# 5
pokedex["Type"] = ["Psychic", "Water/Grass", "Normal", "Normal", "Ghost/Poison"]  # this adds a column!

# 6
import numpy as np
pokedex["HP"] = np.random.randint(1,255,size=5)  # this also adds a column (with 5 values)

# 7
print(pokedex["HP"])

# 8
print(pokedex[["Pokemon Name", "Type"]])

# 9
pokedex.iloc[2]["Type"]

# 10
pokedex.loc[pokedex["Pokemon Name"] == "Meowth"][["Type", "HP"]]


