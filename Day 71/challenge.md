#### Day 71: Data Exploration with Pandas: College Major
**Challenge:** Use Pandas to explore a dataset about college majors.

```python
import pandas as pd

data = pd.read_csv('college_majors.csv')
print(data.head())
print(data.describe())
print(data['Major'].value_counts())
```


