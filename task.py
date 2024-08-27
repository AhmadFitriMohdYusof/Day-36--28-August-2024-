def check_positive_number(num):
    if num < 0:
        raise ValueError("The number must be positive!")
    return num


try:
    check_positive_number(-5)
except ValueError as e:
    print(e)

def check_positive_number(num):
    if num < 0:
        raise ValueError("The number must be positive!")
    return num

try:
    user_input = float(input("Enter a positive number: "))
    result = check_positive_number(user_input)
    print("Success! You entered a positive number:", result)
except ValueError as e:
    print("Error:", e)
