import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('space_race.csv')
data['Date'] = pd.to_datetime(data['Date'])

# Analysis: Number of launches per country
launches_per_country = data['Country'].value_counts()
print(launches_per_country)

# Visualization: Number of launches over time
plt.figure(figsize=(10, 6))
for country in data['Country'].unique():
    country_data = data[data['Country'] == country]
    plt.plot(country_data['Date'], country_data['Launches'], label=country)

plt.title('Space Race: Number of Launches Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Launches')
plt.legend()
plt.show()
