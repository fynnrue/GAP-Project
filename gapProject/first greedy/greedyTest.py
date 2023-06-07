# test of the algorithms

from greedyRatio import start as s1
from greedyCost import start as s2
import os

# choose which instances to test here, e.g. "A" or "B"
instance = "C"

with os.scandir("./instances/" + instance + "/") as entries:
    files = [(instance + "/" + entry.name) for entry in entries if entry.is_file()]

result = [{} for _ in range(len(files))]

i = 0
for file in files:
    status1, costs1 = s1(file)
    status2, costs2 = s2(file)

    tempResult = {
        "status1": status1,
        "costs1": costs1,
        "status2": status2,
        "costs2": costs2,
        "differenz": costs1-costs2
    }
    result[i] = tempResult

    i += 1

    print("\n---------------------")

print("\n")


print("ratio vs cost:")
for element in result:
    print(element)