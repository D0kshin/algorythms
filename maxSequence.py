startSequence = str(input("начальная последовательность:")).split(" ")
startSequence = [int(x) for x in startSequence]
sequencesCount = []

for i, char in enumerate(startSequence):
    sequencesCount.append(1)
    if i != 0:
        subsequence = startSequence[:i+1]
        mbAnswers = []
        for subIndex, number in enumerate(subsequence[::-1]):
            globalIndex = i - subIndex
            if globalIndex != 0:
                if startSequence[i] > startSequence[globalIndex - 1]:
                    mbAnswers.append(sequencesCount[globalIndex - 1])
        if len(mbAnswers) != 0:        
            sequencesCount[i] += max(mbAnswers)

maxCount = max(sequencesCount)
ind = sequencesCount.index(maxCount)
tmp = startSequence[ind]
res = [tmp]
for x in startSequence[ind::-1]:
    if x < tmp:
        tmp = x
        res.append(x)
print(*res[::-1])
