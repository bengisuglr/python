def calculateAverage(listOfDatapoints):
    sum = 0
    for datapoint in olddata: #repeats task for all items in the list
    sum = sum + datapoint
    avg = sum / len(olddata)
    return avg

phlevels = [7.1, 7.5, 7.3, 6.9, 7.2, 7.4, 7.2, 7.4, 6.9, 6.8, 5.0, 5.1, 5.9]
# calculate the avg. of all data except past (latest) three
length = len(phlevels)
avgOld = calculateAverage(phlevels[:length-3])

# calculate avg of past three
latestdata = phlevels[length - 3 :] # second one empty means till the end
print(latestdata)
sum = 0
for datapoint in latestdata:
    sum = sum + datapoint
avgLatest = sum / len(latestdata)
# calculate deviation absolute
devAbs = abs(avgLatest - avgOld)
#calculate deviation percentage
devPercent = devAbs / avgOld
#if deviation is > 10%  (0.1) then sound an alarm
if devPercent > 0.10: #conditional code execution
    print("Quality control alarm!")
else:
    print("All is ok!")
