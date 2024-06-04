#### Day 25: Working with CSV Data and the Pandas Library
**Challenge:** Read data from a CSV file, process it using pandas, and output the results.

```python
import pandas as pd

# Reading CSV data
data = pd.read_csv("example.csv")
print("CSV data:")
print(data)

# Processing data
average_value = data["column_name"].mean()
print(f"Average value in column 'column_name': {average_value}")

# Writing data to a new CSV file
data["new_column"] = data["column_name"] * 2
data.to_csv("output.csv", index=False)
print("Processed data written to output.csv")
```


