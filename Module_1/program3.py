import math

# Get input from the user and convert to float
user_input = float(input("Enter a floating-point number: "))

# Calculate the values
square = user_input * user_input
cube = user_input * user_input * user_input
square_root = math.sqrt(user_input)  # Note: This will crash if you enter a negative number!
ceiling_value = math.ceil(user_input)
floor_value = math.floor(user_input)
absolute_value = abs(user_input)
variable_type = type(user_input)
memory_address = id(user_input)

# Print the results
print()
print("Original Number:", user_input)
print("1. Square:", square)
print("2. Cube:", cube)
print("3. Square Root:", square_root)
print("4. Ceiling Value:", ceiling_value)
print("5. Floor Value:", floor_value)
print("6. Absolute Value:", absolute_value)
print("7. Type of the Variable:", variable_type)
print("8. Memory Address (ID):", memory_address)
