import pandas as pd
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt

data = pd.read_csv('handwashing.csv')
before = data[data['period'] == 'before']
after = data[data['period'] == 'after']

t_stat, p_val = stats.ttest_ind(before['deaths'], after['deaths'])
print("t-statistic:", t_stat, "p-value:", p_val)

sns.histplot(before['deaths'], color='blue', label='Before', kde=True)
sns.histplot(after['deaths'], color='red', label='After', kde=True)
plt.legend()
plt.title('Distribution of Deaths Before and After Handwashing')
plt.show()
