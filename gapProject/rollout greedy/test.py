import os

print(os.getcwd())

with os.scandir("./instances/") as entries:
    for entry in entries:
        print(entry)