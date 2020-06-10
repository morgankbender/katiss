# Problem: https://open.kattis.com/problems/jobexpenses

# Get input. Note: if first input is 0, there is no second input
n = int(input(""))
all_trans = []
if n > 0:
    all_trans = input("").split(" ")

# Init var
expenses = 0

# Check for negative values and add their absolute value to
# the total expenses counter
for str_trans in all_trans:
    trans = int(str_trans)
    if trans < 0:
        expenses += abs(trans)

# Print total expenses value
print(expenses)
