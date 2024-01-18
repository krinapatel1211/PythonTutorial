# the overtime multiplier.
base_hours = 40       # Base hours per week
ot_multiplier = 1.5   # Overtime multiplier

# Get the hours worked and the hourly pay rate from users.
hours_worked = int(input("Enter Hours worked: "))
hourly_pay_rate = float(input("Enter Hourly Pay rate: "))
overtime_hours = int(input("Enter overtime hours worked: "))

# Calculate and display the gross pay.
if hours_worked > base_hours:
    # Calculate the gross pay with overtime.
    # First, get the number of overtime hours worked
    # Calculate the amount of overtime pay.
    overtime_pay = overtime_hours * hourly_pay_rate * ot_multiplier

    # Calculate the gross pay.
    gross_pay = base_hours * hourly_pay_rate + overtime_pay
else:
    # Calculate the gross pay without overtime.
    gross_pay = hours_worked * hourly_pay_rate

# Display the gross pay.
print("Gross Pay = ", gross_pay)
