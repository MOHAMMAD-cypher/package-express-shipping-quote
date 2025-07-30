# Display the welcome message
print("Welcome to Package Express. Please follow the instructions below.")

# Prompt the user for the package weight
weight = float(input("Please enter the package weight: "))

# Check if the package is too heavy
if weight > 50:
    print("Package too heavy to be shipped via Package Express. Have a good day.")
    exit()  # Exit the program if the weight is too high

# Prompt for package width
width = float(input("Please enter the package width: "))

# Prompt for package height
height = float(input("Please enter the package height: "))

# Prompt for package length
length = float(input("Please enter the package length: "))

# Calculate the sum of dimensions
dimension_total = width + height + length

# Check if the dimensions are too large
if dimension_total > 50:
    print("Package too big to be shipped via Package Express.")
    exit()  # Exit if the combined size is too large

# Calculate the shipping quote using the provided formula:
# (width * height * length) * weight / 100
quote = (width * height * length * weight) / 100

# Display the result formatted as a dollar amount
print(f"Your estimated total for shipping this package is: ${quote:.2f}")
print("Thank you!")
