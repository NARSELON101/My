from itertools import *
class Solution:
    def threeSum(self, nums):
        self.rtn = []
        flag = 0
        for i in combinations(nums, 3):
            if sum(i) == 0:
                for j in permutations(i, 3):
                    if list(j) in rtn:
                        flag = 1
                if flag == 0:
                    i = list(i)
                    self.rtn.append(i)
        return self.rtn

print(Solution().threeSum([0,1,1]))


