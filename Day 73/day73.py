import pandas as pd

sets = pd.read_csv('lego_sets.csv')
themes = pd.read_csv('lego_themes.csv')

merged = sets.merge(themes, on='theme_id')
theme_counts = merged['theme_name'].value_counts()

print(theme_counts)
