import sys

def collatzConjectureStoppingTime(curNum, curCount):
    if (curNum == 1):
        return curCount
    elif (curNum % 2 == 1):
        return collatzConjectureStoppingTime((3 * curNum) + 1, curCount + 1)
    elif (curNum % 2 == 0):
        return collatzConjectureStoppingTime(curNum / 2, curCount + 1)
    else:
        print("Critical Error: Exiting")
        return curCount
    
def greatestStoppingTime(inp):
    curHighestNum = 1
    curHighestMark = 0
    for i in range(inp):
        result = collatzConjectureStoppingTime(i + 1, 0)

        if (result > curHighestMark):
            curHighestMark = result
            curHighestNum = i + 1

    print("Collatz stopping time scanned from 1 to " + str(inp))
    print("Num: " + str(curHighestNum))
    print("Stopping Time: " + str(curHighestMark))
    return [curHighestNum, curHighestMark]

def collatzStepsTupleList(num):
    # Initialized variables
    curNum = num
    stepCount = 1
    
    # List should be composed of tuples of the form (stepCount, value)
    list = []

    while(curNum != 1):
        list.append((stepCount, curNum))

        if (curNum % 2 == 1):
            curNum = (curNum * 3) + 1
        elif (curNum % 2 == 0):
            curNum = int(curNum / 2)
        else:
            print("Critical Error: Exiting")
            return list
        
        stepCount = stepCount + 1
    
    list.append((stepCount, 1))

    return list


def main():
    use = int(sys.argv[1])

    if use == 1:
        inp = int(sys.argv[2])
        result = collatzConjectureStoppingTime(inp, 0)
        print("Stopping Time of " + str(inp) + ": " + str(result))
    elif use == 2:
        inp = int(sys.argv[2])
        greatestStoppingTime(inp)
    elif use == 3:
        inp = int(sys.argv[2])
        result = collatzStepsTupleList(inp)
        print(result)
    else:
        print("Incorrect Program Usage: Invalid Use-Case Number (" + str(use) + ")")

main()