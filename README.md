Healthcare in Different States
This project uses boxplots to explore how hospitals in different U.S. states charge patients for medical procedures. The dataset comes from the U.S. Health and Human Services Department and focuses on the DRG for chest pain.

What the project does
Loads the healthcare dataset.

Filters the data to only include chest pain diagnoses.

Separates the data by state.

Creates a boxplot for one state.

Creates boxplots for all states.

Compares the distributions of average covered charges across states.

Files
healthcare.csv — the dataset used in the project.

Python script or notebook containing the boxplot analysis.

Requirements
Python

pandas

matplotlib

NumPy

codecademylib3_seaborn if you are running this in Codecademy

How to run
Make sure healthcare.csv is in the same folder as the script.

Run the Python file or notebook.

Follow the code to generate the boxplots.

What you can learn
Which states have the highest median charges.

Which states have the widest spread in charges.

Which states have the most outliers.

Example code
python
import codecademylib3_seaborn
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

healthcare = pd.read_csv('healthcare.csv')
chest_pain = healthcare[healthcare['DRG Definition'] == '313 - CHEST PAIN']
states = chest_pain['Provider State'].unique()
datasets = []
for state in states:
    datasets.append(chest_pain[chest_pain['Provider State'] == state][' Average Covered Charges '].values)

plt.figure(figsize=(20, 6))
plt.boxplot(datasets, labels=states)
plt.show()
Notes
The Provider State column is used to group hospitals by state.

The Average Covered Charges column includes spaces in the name, so type it exactly as written.
