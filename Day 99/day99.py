import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('police_deaths.csv')

# Analysis: Number of deaths per state
deaths_per_state = data['State'].value_counts()
print(deaths_per_state)

# Visualization: Deaths by race
plt.figure(figsize=(10, 6))
sns.countplot(data=data, x='Race', order=data['Race'].value_counts().index)
plt.title('Deaths involving Police by Race')
plt.xlabel('Race')
plt.ylabel('Number of Deaths')
plt.show()

# Visualization: Deaths over time
data['Date'] = pd.to_datetime(data['Date'])
data['Year'] = data['Date'].dt.year
deaths_per_year = data['Year'].value_counts().sort_index()

plt.figure(figsize=(10, 6))
sns.lineplot(data=deaths_per_year)
plt.title('Deaths involving Police Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Deaths')
plt.show()
