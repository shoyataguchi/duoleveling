# Get input from the user
input1 = input("Enter the first integer: ")
input2 = input("Enter the second integer: ")


# Convert the input strings to integers
# Use a try-except block to handle potential errors if the user enters non-interface
try:
    num1 = int(input1)
    num2 = int(input2)
    
    if num1 > num2:
        print(f"The first integer is larger than the second")
    elif num1 == num2:
        print(f"The first integer is equal to the second")
    else:
        print(f"The first integer is smaller than the second")

except ValueError:
    print(f"Invalid input. Please enter only integers.")