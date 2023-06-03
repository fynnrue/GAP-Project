# greedy algorithm to find a solution for the GAP
# where the job with the smallest cost is chosen

import sys

# instance data
costs = []
resources = []
capacity = []
agentsArr = []
jobsArr = []

def assignJobs():
    overallCosts = 0

    # while not all jobs have been assigned search
    while len(jobsArr) != 0:
        smallestCost = float('inf')
        smallestResource = 0
        smallestAgent = -1
        smallestJob = -1

        # only look at agents and jobs that have not been assigned
        for a in agentsArr:
            for j in jobsArr:
                cost = costs[a][j]
                resource = resources[a][j]

                if cost < smallestCost:
                    if (capacity[a] - resource) >= 0:
                        smallestAgent = a
                        smallestJob = j
                        smallestCost = cost
                        smallestResource = resource

        # check if no fitting job was found
        if smallestAgent == -1 or smallestJob == -1:
            return -1, overallCosts
        
        overallCosts += costs[smallestAgent][smallestJob]
        
        # check if agent from chosen job has a capacity of 0 and removes it if yes
        capacity[smallestAgent] -= smallestResource
        if capacity[smallestAgent] == 0:
            agentsArr.remove(smallestAgent)

        # removes chosen job from available ones
        jobsArr.remove(smallestJob)
        
    return 1, overallCosts

def findCosts(co, re, ca, aA, jA):
    global costs, resources, capacity, agentsArr, jobsArr

    costs = co
    resources = re
    capacity = ca
    agentsArr = aA
    jobsArr = jA

    status, overallCosts = assignJobs()
    return status, overallCosts