# test of the algorithms

from randomHeuristic import randomHeuristik
import os

# choose which instances to test here, e.g. "A" or "B"
instance = "C"

with os.scandir("./instances/" + instance + "/") as entries:
    files = [(instance + "/" + entry.name) for entry in entries if entry.is_file()]

result = []

for file in files:
    bestAssignment, bestCost, capacity = randomHeuristik(file)
    result.append(bestCost)
    print("\n---------------------")

print("\n")
print(result)