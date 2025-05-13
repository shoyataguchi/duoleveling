# Get input from the user
input1 = input("Enter the first integer: ")
input2 = input("Enter the second integer: ")
input3 = input("Enter the Third Integer:")

# Convert the input strings to integers
# Use a try-except block to handle potential errors if the user enters non-interface
try:
    num1 = int(input1)
    num2 = int(input2)
    num3 = int(input3)

    #add the two integers
    sum_result = num1 + num2 + num3

    # Print the result
    print(f"The sum of {num1} , {num2} and {num3} is: {sum_result}")

except ValueError:
    print(f"Invalid input. Please enter only integers.")
