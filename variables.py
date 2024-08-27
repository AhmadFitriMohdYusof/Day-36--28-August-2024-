x = 10  # Global variable

def print_global():
    print(x)  # Accessing the global variable

print_global()  # Output: 10


x = 10  # Global variable

def modify_global():
    global x  # Declare that we want to use the global variable 'x'
    x = 20  # Modify the global variable

modify_global()
print(x)  # Output: 20
