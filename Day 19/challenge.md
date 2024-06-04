#### Day 19: Instances, State and Higher Order Functions
**Challenge:** Create a higher-order function that takes another function and a list of numbers as arguments, and applies the function to each number in the list.

```python
def apply_function(func, numbers):
    return [func(num) for num in numbers]

def square(number):
    return number ** 2

nums = [1, 2, 3, 4, 5]
squared_nums = apply_function(square, nums)
print(squared_nums)
```


