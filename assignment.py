counter = 0
def increment_counter():
    global counter
    counter += 1
    print(f"Global counter: {counter}")

def reset_counter():
    counter = 0  # Local variable
    print(f"Local counter: {counter}")

increment_counter()  # Global counter should be 1
increment_counter()  # Global counter should be 2
increment_counter()  # Global counter should be 3
reset_counter()      # Local counter should be 0

# Print the global counter after each function call
print(f"Global counter after reset: {counter}")

# File and Directory Operations
import os

# Print the current working directory
cwd = os.getcwd()
print(f"Current working directory: {cwd}")

# List all files and directories in the current working directory
files_and_dirs = os.listdir(cwd)
print(f"Files and directories in {cwd}: {files_and_dirs}")

# Create a new directory called test_dir
os.mkdir("test_dir")

# Change the working directory to test_dir
os.chdir("test_dir")

# Print the new working directory
new_cwd = os.getcwd()
print(f"New working directory: {new_cwd}")

# Create a new file named test_file.txt inside test_dir
with open("test_file.txt", "w") as f:
    f.write("This is a test file.")

# List files in the new directory
files_in_test_dir = os.listdir(new_cwd)
print(f"Files in {new_cwd}: {files_in_test_dir}")

# Delete test_file.txt and test_dir
os.remove("test_file.txt")
os.chdir("..")  # Go back to the parent directory
os.rmdir("test_dir")

# Function to divide numbers with exception handling
def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        result = None
    finally:
        print("Division operation completed.")
    return result

# Get input from the user and perform division
a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))

# Call the divide_numbers function and print the result
result = divide_numbers(a, b)
if result is not None:
    print(f"Result of {a} divided by {b} is: {result}")
