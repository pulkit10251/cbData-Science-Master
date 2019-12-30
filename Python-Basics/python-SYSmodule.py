import sys


def printData():
    print(sys.argv)

    
def printSum():
    print(int(sys.argv[1])+int(sys.argv[2]))
    
printData()
# printSum()

print(sys.version)
print(sys.path)


 # print(sys.maxint)
print(sys.maxsize)
print(sys.stdout)
print(type(sys.stdout))