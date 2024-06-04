import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

data = pd.read_csv('nobel_prize.csv')
sns.histplot(data['year'])
plt.title('Nobel Prizes by Year')
plt.show()

fig = px.bar(data, x='category', y='age', color='gender', title='Nobel Prize Winners')
fig.show()
