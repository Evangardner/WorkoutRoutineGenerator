#takes weight and bench and returns a number representative of the ranking
def compareBench(weight, bench):
    ratio = (bench/weight)*100
    if ratio<70:
        return 0
    elif ratio<90:
        return 1
    elif ratio<130:
        return 2
    elif ratio<200:
        return 3
    elif ratio>=200:
        return 4

#takes weight and squat and returns a number representative of the ranking
def compareSquat(weight, squat):
    ratio = (squat/weight)*100
    if ratio<85:
        return 0
    elif ratio<120:
        return 1
    elif ratio<160:
        return 2
    elif ratio<240:
        return 3
    elif ratio>239:
        return 4

#takes weight and deadlift and returns a number representative of the ranking
def compareDeadLift(weight, dl):
    ratio = (dl/weight)*100
    if ratio<100:
        return 0
    elif ratio<140:
        return 1
    elif ratio<180:
        return 2
    elif ratio<240:
        return 3
    elif ratio>=280:
        return 4
#method that takes weight and all the respective one rep maximums of exercises
#returns array with bench, squat, and deadlift ratios in that order
def compareAverages(weight, bench, squat, dl):
    benchRatio = compareBench(weight,bench)
    squatRatio = compareSquat(weight,squat)
    dlRatio = compareDeadLift(weight,dl)
    return [benchRatio,squatRatio,dlRatio]

#converts number that compare methods return to corresponding rank
#returns string of rank
def toRank(num):
    s = ""
    if num==0 :
        s="untrained"
    elif num==1 :
        s="novice"
    elif num==2 :
        s="intermediate"
    elif num==3 :
        s="advanced"
    elif num==4 :
        s="elite"
    return s
#print method that takes array of the averages and prints formatted output of the values
def printRatios(averages):
    print"Ratios of exercise to weight compared to averages"
    print"Bench Ratio:", toRank(averages[0])
    print"Squat Ratio:", toRank(averages[1])
    print"Deadlift Ratio:",toRank(averages[2])
printRatios(compareAverages(200,200,200,200))
