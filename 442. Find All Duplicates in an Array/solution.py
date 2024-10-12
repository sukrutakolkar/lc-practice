from typing import List
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []

        for val in nums:
            val = abs(val) # abs. value because element can be already marked
            # check if element is already visited
            if nums[val-1] < 0:
                res.append(val)
            # mark element as visited
            else:
                nums[val-1] = -nums[val-1]

        return res
    
if __name__ == "__main__":
    sol = Solution()
    res = sol.findDuplicates([4,3,2,7,8,2,3,1])
    print(res)
    assert res == [2,3]
