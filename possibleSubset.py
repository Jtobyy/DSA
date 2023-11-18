from collections import defaultdict

def possibleSubsets(arr):
    res = [{i} for i in arr]

    for i in arr:
        curRes = list(res)
        for s in curRes:
            newS = set(s)
            if i not in s:
                newS.add(i)
                res.append(newS)

    tupleRes = defaultdict(int)
    for s in res:
        tupleRes[tuple(s)] += 1

    finalRes = [list(t) for t in tupleRes]

    return finalRes

print(possibleSubsets([1, 2, 3, 4, 5]))
