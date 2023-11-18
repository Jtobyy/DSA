from possibleSubset import possibleSubsets
from functools import reduce
import operator

def solution(arr):
    subSets = possibleSubsets(arr)
    res = []
    
    for arr in subSets:
        res.append(reduce(operator.add, arr))

    return res[-1] - res[-2]


print(solution([1, 2,3,4,5]))
