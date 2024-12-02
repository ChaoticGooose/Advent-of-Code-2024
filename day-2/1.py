from itertools import tee

def getReports(file: str) -> list:
    f = open(file, "r")
    
    reports = list()
    for row in f:
        reports.append(row.strip().split())
    
    return reports

def pairwise(iterable):
    a,b = tee(iterable)
    next(b, None)
    return zip(a,b)

def main():
    reports = getReports("input")
    
    safe = 0
    for row in reports:
        """
        Lord have mercy on me.
        This is such shit code, there must be a better solution than this
        """
        it = iter(row)
        status = -1
        for pair in pairwise(it):
            p = int(pair[0])-int(pair[1])
            if status == -1 and 1<=p<=3:
                status = 1
            if status == -1 and -3<=p<=-1:
                status = 0
            if status == 0 and 1<=p<=3:
                break
            if status == 1 and -3<=p<=-1:
                break
            if p==0 or p>3 or p<-3:
                break
        else:
            safe += 1

    print(safe)
main()
