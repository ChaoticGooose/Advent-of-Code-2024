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
    right = {i:right.count(i) for i in set(left)} # Convert right list to freq dict

    sum = 0
    for entry in left:
        sum += (entry*right[entry])

    print(sum)

main()
