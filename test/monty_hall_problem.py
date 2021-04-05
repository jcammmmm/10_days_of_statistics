import random
"""
A :  the contestant does no change its election
B :  the contestant chages its election
"""
def main():
    runs = 10
    okA = 0
    okB = 0
    for _ in range(runs):
        pA, pB = runSimulation(10_000)
        if abs(pA - 1/3) < 0.1:
            okA += 1
        if abs(pB - 2/3) < 0.1:
            okB += 1
    
    if okA == runs and okB == runs:
        print("SIMULATION CERTIFIES THEORY!")
    else:
        print("THE THEORY WAS WRONG!")
    

        

def runSimulation(totalCases):
    # participant does not change election
    winsA = 0
    for _ in range(totalCases):
        contest = nextContest()
        doorSel = random.randint(0, 2)
        if contest[doorSel] == 'C':
            winsA += 1
    print(winsA/totalCases)

    # participant changes election
    winsB = 0
    for _ in range(totalCases):
        contest = nextContest()
        curSel = random.randint(0, 2)
        goatDoor = locateGoat(contest, curSel)
        newSel = newSelection(curSel, goatDoor)
        if contest[newSel] == 'C':
            winsB += 1
    print(winsB/totalCases)
    
    return winsA/totalCases, winsB/totalCases



def locateGoat(contest, selection):
    loc = -1
    for i in range(len(contest)):
        if i != selection and contest[i] == 'G':
            loc = i
    return loc

def newSelection(curSel, goatDoor):
    ava = [0, 1, 2]
    ava.remove(curSel)
    ava.remove(goatDoor)
    return ava[0]

def nextContest():
    games = [
        ['C', 'G', 'G'],
        ['G', 'C', 'G'],
        ['G', 'G', 'C']
    ]
    return games[random.randint(0, 2)]

if __name__ == '__main__':
    main()