#### Day 100: Portfolio Project - Predicting Earnings using Multivariable Regression
**Challenge:** Build a machine learning model to predict earnings using multivariable regression.

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load data
data = pd.read_csv('earnings.csv')

# Select features and target variable
X = data[['Experience', 'Education', 'Age']]
y = data['Earnings']

# Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# Visualize the results
plt.scatter(y_test, y_pred)
plt.xlabel('Actual Earnings')
plt.ylabel('Predicted Earnings')
plt.title('Actual vs Predicted Earnings')
plt.show()
```

