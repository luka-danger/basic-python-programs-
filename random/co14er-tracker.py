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

def addPeak(peak, totalSummits, range, classRank): 
    newPeak = {}
    newPeak["peak"] = peak
    newPeak["total_summits"] = totalSummits
    newPeak["range"] = range
    newPeak["class"] = classRank
    co14erTracker.append(newPeak)

addPeak("Longs", 1, "Front", 3)
addPeak("Crestone Needle", 1 ,"Sangre De Cristo", 3)

print(co14erTracker)