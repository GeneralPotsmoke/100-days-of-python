import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('housing_prices.csv')
sns.lmplot(x='square_feet', y='price', data=data)
plt.title('Linear Regression: Square Feet vs Price')
plt.show()
