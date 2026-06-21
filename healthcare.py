import codecademylib3_seaborn
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

healthcare = pd.read_csv("healthcare.csv")

# TASK 1
print(healthcare.head())

# TASK 2
print(healthcare["DRG Definition"].unique())

# TASK 3
chest_pain = healthcare[healthcare['DRG Definition'] == '313 - CHEST PAIN']

# TASK 4
alabama_chest_pain = chest_pain[chest_pain['Provider State'] == "AL"]

# TASK 5
costs = alabama_chest_pain[' Average Covered Charges '].values

# TASK 6 (Comment out for Task 7)
# plt.boxplot(costs)
# plt.show()

# TASK 7
states = chest_pain['Provider State'].unique()

# TASK 8
datasets = []
for state in states:
    datasets.append(chest_pain[chest_pain['Provider State'] == state][' Average Covered Charges '].values)

# TASK 9 & 10
plt.figure(figsize=(20, 6))
plt.boxplot(datasets, labels=states)
plt.show()

# TASK 11 - FIXED VERSION
state_median_pairs = []
for state in states:
    charges = chest_pain[chest_pain['Provider State'] == state][' Average Covered Charges '].values
    median_val = np.median(charges)
    state_median_pairs.append((state, median_val, charges))

state_median_pairs.sort(key=lambda x: x[1])

states_sorted = [pair[0] for pair in state_median_pairs]
datasets_sorted = [pair[2] for pair in state_median_pairs]

plt.figure(figsize=(20, 6))
plt.boxplot(datasets_sorted, labels=states_sorted)
plt.show()
