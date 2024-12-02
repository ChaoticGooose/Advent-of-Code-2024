def getDistances(file):
    left = list()
    right = list()

    f = open(file, "r")

    for line in f:
        current = line.split("   ")
        left.append(int(current[0].strip()))
        right.append(int(current[1].strip()))

    return left,right
        


def main():
    left, right = getDistances("input")
    left.sort()
    right.sort()

    sum = 0
    for i in range(0, len(left)):
        sum+= abs(left[i]-right[i])
        
    print(sum)

main()