co14erTracker = [
    {
    "peak": "Quandary Peak", 
     "total_summits": 1,
     "range": "Tenmile",
     "class": 1
     } , 
     {"peak": "Mt. Bierstadt",
      "total_summits": 2,
      "range": "Front",
      "class": 2
      }
]

# Manually input information on terminal 
def addNew14er(): 
    # Create new dictionary 
    new14er = {}
    new14er["peak"] = input("Please enter a peak: ")
    new14er["total_summits"] = input("How many times have you summited?: ")
    new14er["range"] = input("What range is it in?: ")
    new14er["class"] = input("What class ranking is it?: ")
    # Add dictionary to co14erTracker dictionary 
    co14erTracker.append(new14er)

# Takes arguments when function is called 
def addPeak(peak, totalSummits, range, classRank): 
    newPeak = {}
    newPeak["peak"] = peak
    newPeak["total_summits"] = totalSummits
    newPeak["range"] = range
    newPeak["class"] = classRank
    co14erTracker.append(newPeak)

addPeak("Longs", 1, "Front", 3)
addPeak("Crestone Needle", 1 ,"Sangre De Cristo", 3)
addNew14er()

print(co14erTracker)