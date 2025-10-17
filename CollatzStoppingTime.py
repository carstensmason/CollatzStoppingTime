import sys

def CollatzConjectureFunc(curNum, curCount):
    if (curNum == 1):
        return curCount
    elif (curNum % 2 == 1):
        return CollatzConjectureFunc((3 * curNum) + 1, curCount + 1)
    elif (curNum % 2 == 0):
        return CollatzConjectureFunc(curNum / 2, curCount + 1)
    else:
        print("Critical Error: Exiting")
        return curCount

def main():
    inp = int(sys.argv[1])
    print("Number to test: " + str(inp))
    print(CollatzConjectureFunc(inp, 0))

main()