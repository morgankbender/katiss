# Problem: https://open.kattis.com/problems/weakvertices

# External imports
import sys

# Problem input gives an unknown amount of test cases to be processed,
# with a sentinel value of -1. Each test case may span a different number
# of input lines
while True:
    # Get number of vertices from input. Note: -1 is supposed to indicate
    # end of input. To handle this, the program will "break" when it sees
    # -1, and again when it receives an EOFError
    try:
        num_v = int(input(""))
    except EOFError:
        break
    if num_v == "-1":
        break

    # Get graph from input
    graph = []
    for i in range(num_v):
        graph.append(input("").split(" "))

    # Init var
    n = 3
    weak_vert = [True] * num_v
    checked_starting = [False] * num_v

    # Recursive depth first search algorithm, with controls to only reach a depth of n
    def dfs(visited, vert, path):
        # Save that we have visited the current vert and add it the path
        path.append(vert)
        visited[vert] = True

        # Once the path has reached length n, we can check if it forms a cycle
        if len(path) == n:
            if graph[vert][path[0]] == "1":
                for v in path:
                    weak_vert[v] = False
        # If the path has not yet reached length n, we will recurse
        else:
            for v in range(num_v):
                if graph[vert][v] == "1" and visited[v] is False:
                    dfs(visited[:], v, path[:])

    # Perform dfs that starts at each vert (minus redundancies)
    for i in range(num_v - (n - 1)):
        checked_starting[i] = True
        dfs(checked_starting[:], i, [])

    # Get final list of vert that are "weak" (not part of a cycle
    # of length n) that can be printed on a single line
    output = []
    for i in range(num_v):
        if weak_vert[i] is True:
            output.append(i)
    print(*output)
