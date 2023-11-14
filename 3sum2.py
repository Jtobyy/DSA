from collections import defaultdict 

class Solution(object):
    def middle_of_three(self, a, b, c):
        if a <= b <= c or c <= b <= a:
            return b
        elif b <= a <= c or c <= a <= b:
            return a
        else:
            return c

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        i = 0
        j = 1
        res = []
        combos = set()
        l = len(nums)

        # structure to keep track of amount of each elements present
        numsDict = defaultdict(int)
        for n in nums:
            numsDict[n] += 1

        while i < l and j < l - 1:
            p1 = nums[i]
            p2 = nums[j]

            s = p1 + p2

            # get value needed from the rest
            d = 0 - s
            amountNeeded = 1
            if d == p1 and d == p2:
                amountNeeded = 3
            elif d == p1 or d == p2:
                amountNeeded = 2

            if d in numsDict and numsDict[d] >= amountNeeded:
                # sort the 3 items so we can easily search for duplicates
                newTriplet = [min(p1, p2, d), self.middle_of_three(p1, p2, d), max(p1, p2, d)]
                if str(newTriplet) not in combos:
                    combos.add(str(newTriplet))
                    res.append([p1, p2, d])
    
            j += 1
            if j == l - 1:
                i += 1
                j = i + 1

        return res

if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]
    nums = [0,1,1]
    nums = [0,0,0]
    solution = Solution()
    res = solution.threeSum(nums)
    print(res)
