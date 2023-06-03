# greedy algorithm to find a solution for the GAP
# where the job with the smallest cost/resource ratio is chosen

import sys
from readData import getData

# instance data
costs = []
resources = []
capacity = []
amntAgents = 0
amntJobs = 0

def assignJobs():
    overallCosts = 0

    agentsArr = [i for i in range(amntAgents)]
    jobsArr = [i for i in range(amntJobs)]

    # while not all jobs have been assigned search
    while len(jobsArr) != 0:
        smallestRatio = float('inf')
        smallestResource = 0
        smallestAgent = -1
        smallestJob = -1

        # only look at agents and jobs that have not been assigned
        for a in agentsArr:
            for j in jobsArr:
                cost = costs[a][j]
                resource = resources[a][j]

                ratio = 5*cost + resource

                if ratio < smallestRatio:
                    if (capacity[a] - resource) >= 0:
                        smallestAgent = a
                        smallestJob = j
                        smallestRatio = ratio
                        smallestResource = resource

        # check if no fitting job was found
        if smallestAgent == -1 or smallestJob == -1:
            print("Greedy algorithm couldnt assign all jobs to an agent!")
            print("Overall costs:", overallCosts)
            print("Jobs that still need to be assigned:", jobsArr)
            print("Remaining capacity of the agents:", capacity)
            return -1, overallCosts
        
        overallCosts += costs[smallestAgent][smallestJob]
        
        # check if agent from chosen job has a capacity of 0 and removes it if yes
        capacity[smallestAgent] -= smallestResource
        if capacity[smallestAgent] == 0:
            agentsArr.remove(smallestAgent)

        # removes chosen job from available ones
        jobsArr.remove(smallestJob)
        

    print("Overall costs:", overallCosts)
    print("Jobs that still need to be assigned:", jobsArr)
    print("Remaining capacity of the agents:", capacity)
    return 1, overallCosts

def start(file):
    global costs, resources, capacity, amntAgents, amntJobs
    data = getData(file)

    costs, resources, capacity, amntAgents, amntJobs = data

    print("\n", file, "greedyRatio")

    return assignJobs()