class Solution(object):
    """Couln't work for [-2, 0, 1, 1, 2],
    once it moves the front and back pointers, couldn't find a way to move it back"""
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        i = 0
        j = len(nums) - 1
        res = []

        while i != j:
            p1 = nums[i]
            p2 = nums[j]
            s = p1 + p2
            if s < 0:
                p3 = nums[j-1]
                s += p3
                if s < 0:
                    i += 1
            elif s > 0:
                p3 = nums[i+1]
                s += p3
                if s == 0:
                    res.append([p1, p2, p3])
                i += 1
                j -= 1
            else:
                if 0 in nums:
                    p3 = 0
                    res.append([p1, p2, p3])
                i += 1
                j -= 1

        return res


if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]
    nums = [0,1,1]
    nums = [0,0,0]
    solution = Solution()
    res = solution.threeSum(nums)
    print(res)
