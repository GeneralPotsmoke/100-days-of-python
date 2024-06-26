import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('google_trends.csv', parse_dates=['date'])
data.set_index('date', inplace=True)
monthly_data = data.resample('M').mean()

monthly_data.plot()
plt.title('Google Trends Over Time')
plt.ylabel('Search Interest')
plt.xlabel('Date')
plt.show()
