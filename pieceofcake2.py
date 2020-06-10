# Get input
param = input("").split(" ")

# Init var
cakeHeight = 4
cakeLen = int(param[0])
horCut = int(param[1])
vertCut = int(param[2])

# Put the equation for each of the four pieces into
# a max function and print the result
print(max([
    horCut * vertCut * cakeHeight,
    (cakeLen - horCut) * vertCut * cakeHeight,
    horCut * (cakeLen - vertCut) * cakeHeight,
    (cakeLen - horCut) * (cakeLen - vertCut) * cakeHeight,
]))
