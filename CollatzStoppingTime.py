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


def main():
    use = int(sys.argv[1])

    if use == 1:
        inp1 = int(sys.argv[2])
        result = collatzConjectureStoppingTime(inp1, 0)
        print("Stopping Time of " + str(inp1) + ": " + str(result))
    elif use == 2:
        inp1 = int(sys.argv[2])
        greatestStoppingTime(inp1)
    else:
        print("Incorrect Program Usage: Invalid Use-Case Number (" + str(use) + ")")

main()