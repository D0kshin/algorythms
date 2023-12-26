startSequence = str(input("начальная последовательность:"))
searchSequence = str(input("искомая подпоследовательность:"))

subSecuences = []
sequenceChars = []
countSequences = []

for i in range(1, len(searchSequence) + 1):
    subSecuences.append(searchSequence[0:i])
    sequenceChars.append(searchSequence[i - 1])
    countSequences.append(0)

for char in startSequence:
    if char in sequenceChars:
        charIndexes = [i for i in range(len(sequenceChars)) if char == sequenceChars[i]] #найти все вхождения (индексы всех вхождений)
        for index in charIndexes[::-1]:#в обратную обновитть счетчики(это правильно при повторениях)
            if index == 0:
                countSequences[0] += 1
            else:
                countSequences[index] += countSequences[index - 1]

for i, x in enumerate(subSecuences):
    print(x, "встретилось - ", countSequences[i], " раз")
            
            