# Problem: https://open.kattis.com/problems/schoolspirit

# Get number of students
n = int(input(""))

# Init vars
scores = [0] * n
group_scores = [0] * (n + 1)


# Method to get group score. Takes one param which is the index of the variable to remove
def get_score(rm_i):
    group_score = 0
    ind = 0

    for j in range(n):
        if j != rm_i:
            group_score += scores[j] * ((4 / 5) ** ind)
            ind += 1

    return group_score / 5


# Get all scores from input
for i in range(n):
    scores[i] = int(input(""))

# Get score with each index removed (go one index past number of students so last
# calculation is removing no student)
for i in range(n + 1):
    group_scores[i] = get_score(i)

# Print last score (score with all students)
print(group_scores[n])

# Print average of all scores where a student is removed
print(sum(group_scores[:n]) / n)
