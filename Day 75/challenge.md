#### Day 75: Beautiful Plotly Charts & Analyzing the Android App Store
**Challenge:** Use Plotly to create interactive charts and analyze data from the Android App Store.

```python
import pandas as pd
import plotly.express as px

data = pd.read_csv('android_apps.csv')
fig = px.scatter(data, x='Rating', y='Reviews', color='Category', size='Installs',
                 hover_name='App', title='Android App Store Analysis')
fig.show()
```


