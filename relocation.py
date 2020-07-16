# Problem: https://open.kattis.com/problems/relocation

# Init vars and get input
params = input("").split(" ")
n = int(params[0])
q = int(params[1])
start_loc = input("").split(" ")
business_loc = [0] * (n + 1)

# Copy the list passed in with start locations. This is to make sure
# they are stored as ints and also to shift everything by one so the
# index matches the business number (0 will be "empty")
for i in range(n):
    business_loc[i+1] = int(start_loc[i])

# Iterate through each query
for i in range(q):
    params = input("").split(" ")

    # If query begins with a 1, the next value is business number
    # and next is its move location
    if params[0] == "1":
        business_loc[int(params[1])] = int(params[2])
    # If query begins with a 2, print the distance between the
    # businesses (indicated by following two values)
    else:
        print(abs(business_loc[int(params[1])] - business_loc[int(params[2])]))

