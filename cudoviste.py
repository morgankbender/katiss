# Problem: https://open.kattis.com/problems/cudoviste

# Get problem params
params = input("").split(" ")
rows = int(params[0])
cols = int(params[1])

# Init vars
parking_map = []
crushed = [0] * 5

# Get parking grid from input
for i in range(rows):
    parking_map.append(input(""))

# Get each possible parking space by checking top left corners
for i in range(rows - 1):
    for j in range(cols - 1):
        symbols = [
            parking_map[i][j],
            parking_map[i][j+1],
            parking_map[i+1][j],
            parking_map[i+1][j+1]
        ]

        # If there are no #s in the spot, it is valid. Calculate
        # how many cars are crushed in this spot and add it to
        # the running totals
        if "#" not in symbols:
            crushed[symbols.count("X")] += 1

# Print how many parking spaces there are at each amount of crushed cars
for value in crushed:
    print(value)