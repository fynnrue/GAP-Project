import sys
from readData import getData
import random
import array
import copy
import math

# program data
filename = ""

# instance data
costs = None
resources = None
capacity = None
amntAgents = 0
amntJobs = 0

# create a random first assignment
def createAssignment(amntAssignTries):
    global capacity

    bestAssignment = array.array('i', [-1]*amntJobs)
    bestNotAssigned = [i for i in range(amntJobs)]
    bestCapacity = []

    # try math.sqrt(amntAgents*amntJobs) times to assign all jobs
    while amntAssignTries < math.sqrt(amntAgents*amntJobs):
        assignment = array.array('i', [-1]*amntJobs)
        notAssigned = []
        tempCapacity = capacity[:]
        jobs = [i for i in range(amntJobs)]

        # choose a random job and a random agent until all jobs are assigned
        while len(jobs) != 0:
            randJob = random.choice(jobs)
            jobs.remove(randJob)

            assigned = False
            agents = [i for i in range(amntAgents)]

            for _ in range(len(agents)):
                randAgent = random.choice(agents)
                agents.remove(randAgent)

                # check if agent has enough capacity to do the job
                if tempCapacity[randAgent] >= resources[randAgent][randJob]:
                    tempCapacity[randAgent] -= resources[randAgent][randJob]
                    assignment[randJob] = randAgent
                    assigned = True
                    break

            if assigned == False:
                notAssigned.append(randJob)
        
        # check if the current assignment is better than the best assignment
        if notAssigned == []:
            return assignment, []
        else:
            if len(notAssigned) < len(bestNotAssigned):
                bestAssignment = assignment
                bestNotAssigned = notAssigned
                bestCapacity = tempCapacity
            amntAssignTries += 1

    capacity = bestCapacity
    return bestAssignment, bestNotAssigned


# assign all jobs that are already assigned to another agent and check if costs get less
def solveGap():
    global capacity

    assignment, notAssigned = createAssignment(0)
    bestAssignment = copy.copy(assignment)
    bestCost = calculateTotalCost(bestAssignment)
    bestCapacity = capacity[:]

    # try to assign all jobs that are already assigned to another agent
    for i in range(50):
        for job in range(amntJobs):
            for agent in range(amntAgents):
                tempCapacity = bestCapacity[:]

                if assignment[job] != -1:
                    if tempCapacity[agent] >= resources[agent][job]:
                        tempCapacity[assignment[job]] += resources[assignment[job]][job]
                        tempCapacity[agent] -= resources[agent][job]

                        assignment[job] = agent
                        cost = calculateTotalCost(assignment)
                        if cost < bestCost:
                            bestAssignment = assignment[:]
                            bestCost = cost
                            bestCapacity = tempCapacity
                            break

                        tempCapacity[assignment[job]] -= resources[assignment[job]][job]
                        tempCapacity[agent] += resources[agent][job]
                        assignment[job] = bestAssignment[job]

    capacity = bestCapacity
    return bestAssignment, notAssigned

# try to assign all remaining jobs that could not be assigned in the initial assign
def assignNotAssigned(bestAssignment, notAssigned):
    for job in notAssigned:
        for agent in range(amntAgents):
            if capacity[agent] >= resources[agent][job]:
                capacity[agent] -= resources[agent][job]
                bestAssignment[job] = agent
                notAssigned.remove(job)
                break

    return bestAssignment, notAssigned


# calculate cost of current assignment
def calculateTotalCost(assignment):
    totalCost = 0
    for job in range(amntJobs):
        agent = assignment[job]
        if agent != -1:  # Check if the job is assigned to an agent
            totalCost += costs[agent][job]
    return totalCost


def randomHeuristik(filename):
    global costs, resources, capacity, amntAgents, amntJobs

    costs, resources, capacity, amntAgents, amntJobs = getData(filename)

    bestAssignment, notAssigned = solveGap()

    if notAssigned != []:
        bestAssignment, notAssigned = assignNotAssigned(bestAssignment, notAssigned)
        if notAssigned != []:
            print("Could not assign jobs:", notAssigned, "\n")

    bestCost = calculateTotalCost(bestAssignment)

    print("Best assignment:", bestAssignment, "\n")
    print("Best cost:", bestCost, "\n")
    print("Best capacity", capacity, "\n")

    return bestAssignment, bestCost, capacity