from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        # DFS Backtrack Tree
        def backTreek(index, combination, total):
            # base cases
            if total == target:
                res.append(list(combination))
                return
            elif index >= len(candidates) or total + candidates[index] > target:
                return

            # Left Leg - explores combinations considering the current candidate
            combination.append(candidates[index])
            backTreek(index, combination, total + candidates[index])
            # Right Leg - explores combinations considering the next candidates
            combination.pop()
            backTreek(index + 1, combination, total)

        backTreek(0, [], 0)
        return res
    
if __name__ == "__main__":
    sol = Solution()
    res = sol.combinationSum([2,3,6,7], 7)
    print(res)
    assert res == [[2,2,3], [7]]
