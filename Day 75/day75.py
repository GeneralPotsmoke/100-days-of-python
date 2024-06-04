import pandas as pd
import plotly.express as px

data = pd.read_csv('android_apps.csv')
fig = px.scatter(data, x='Rating', y='Reviews', color='Category', size='Installs',
                 hover_name='App', title='Android App Store Analysis')
fig.show()
