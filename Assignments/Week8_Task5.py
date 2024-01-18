# This program determines whether a bank customer
# qualifies for a loan.

min_salary = 30000.0  # The minimum annual salary
min_years = 2         # The minimum years on the job

# Get the customer's annual salary.
annual_salary = int(input("Enter customer's annual salary: "))

# Get the number of years on the current job.
years_on_job = float(input("Enter the number of years on the current job: "))

# Determine whether the customer qualifies.
if annual_salary >= min_salary and years_on_job >=2:
    print("Customer qualifys  for a loan")
elif annual_salary < min_salary:
    print("Customer need to make at least minimum salary which is 30000")
elif years_on_job <2:
    print("customer does not qualify for a loan")
