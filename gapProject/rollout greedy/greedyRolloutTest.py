# test of the algorithms

from greedyCostRollout import start
import os

# choose which instances to test here, e.g. "A" or "B"
instance = "A"

with os.scandir("./instances/" + instance + "/") as entries:
    files = [(instance + "/" + entry.name) for entry in entries if entry.is_file()]

files.sort()

result = [{} for _ in range(len(files))]

i = 0
for file in files:
    status, costs = start(file)

    tempResult = {
        "status": status,
        "costs": costs
    }
    result[i] = tempResult

    i += 1

    print(status, costs)
    print("\n---------------------")

print("\n")

for element in result:
    print(element)