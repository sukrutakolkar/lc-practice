from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [nums[0]]

        for n in nums[1:]:
            switched = False
            for r in range(len(res)):
                if n <= res[r]:
                    res[r] = n
                    switched = True
                    break
            if not switched:
                res.append(n)
            #print(res)
        return len(res)
    
if __name__ == "__main__":
    sol = Solution()
    res = sol.lengthOfLIS([10,9,2,5,3,7,101,18])
    print(res)
    assert res == 4
