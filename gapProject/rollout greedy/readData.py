import sys

# program data
filename = ""
file = None

# instance data
costs = None
resources = None
capacity = None
amntAgents = 0
amntJobs = 0


# called from algorithm to get data from file
def getData(file):
    global filename
    filename = file
    
    # read out data from file
    readData()

    # end of program
    return costs, resources, capacity, amntAgents, amntJobs


# reads data from file
def readData():
    # change global variables
    global costs, resources, capacity, amntAgents, amntJobs

    # read file from instances folder
    path = "./instances/" + filename

    # open file if possible
    with open(path, "r") as file:
        firstLine = file.readline()
        firstLineArgs = firstLine.split(" ")

        amntAgents = int(firstLineArgs[1])
        amntJobs = int(firstLineArgs[2])

        costs = [[0 for j in range(amntJobs)] for i in range(amntAgents)]
        resources = [[0 for j in range(amntJobs)] for i in range(amntAgents)]
        capacity = [0 for i in range(amntAgents)]

        file = file.read()
        data = file.split()

        i = 0
        for agent in range(amntAgents):
            for job in range(amntJobs):                       
                costs[agent][job] = int(data[i])
                i += 1
        for agent in range(amntAgents):
            for job in range(amntJobs):
                resources[agent][job] = int(data[i])
                i += 1
        for agent in range(amntAgents):
            capacity[agent] = int(data[i])
            i += 1
    return