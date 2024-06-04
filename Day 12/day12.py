global_variable = "I am global"

def my_function():
    local_variable = "I am local"
    print(local_variable)
    print(global_variable)

my_function()
print(global_variable)
