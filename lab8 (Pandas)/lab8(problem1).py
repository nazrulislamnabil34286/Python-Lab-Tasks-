import pandas as pd

calories = {
    "day1": 420,
    "day2": 380,
    "day3": 390
}

s = pd.Series(calories)

print("Calories:")
print(s)

total_calories = s.sum()

print("\nTotal Calories:", total_calories)