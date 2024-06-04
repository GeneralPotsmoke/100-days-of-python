import pandas as pd

data = pd.read_csv('college_majors.csv')
print(data.head())
print(data.describe())
print(data['Major'].value_counts())
