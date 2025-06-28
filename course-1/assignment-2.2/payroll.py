# Program to calculate gross pay with overtime
# Overtime is 1.5 times the hourly rate for hours worked above 40

# Get input from user
hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

# Convert string inputs to float
hours = float(hours)
rate = float(rate)

# Calculate pay
if hours <= 40:
    # Regular pay for 40 hours or less
    pay = hours * rate
else:
    # Regular pay for first 40 hours + overtime for remaining hours
    regular_pay = 40 * rate
    overtime_hours = hours - 40
    overtime_pay = overtime_hours * (rate * 1.5)
    pay = regular_pay + overtime_pay

print("Pay:", pay) 