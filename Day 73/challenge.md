#### Day 73: Aggregate & Merge Data with Pandas: Analyze the LEGO Dataset
**Challenge:** Use Pandas to aggregate and merge data from a LEGO dataset.

```python
import pandas as pd

sets = pd.read_csv('lego_sets.csv')
themes = pd.read_csv('lego_themes.csv')

merged = sets.merge(themes, on='theme_id')
theme_counts = merged['theme_name'].value_counts()

print(theme_counts)
```


