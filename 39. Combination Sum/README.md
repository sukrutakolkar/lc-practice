# 39. Combination Sum
**Difficulty** - Medium

**Topic(s)** - Array, Backtracking 

### Description
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.
 

Example 1:

>Input: candidates = [2,3,6,7], target = 7
>Output: [[2,2,3],[7]]
>Explanation:
>2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
>7 is a candidate, and 7 = 7.
>These are the only two combinations.

Example 2:

>Input: candidates = [2,3,5], target = 8
>Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:

>Input: candidates = [2], target = 1
>Output: []

### Solution
```python
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
```

### Explanation: 
We use a Backtracking algorithm with DFS tree. Important factor here is to avoid duplicates (permutations) in the final result.

At each node we explore combinations with 2 possibilities:
1. Add the current indexed element to the combination. 
2. Consider the next indexed element to the combination.

Hence, at each node, we get 2 legs explores combinations adding the current element while the right leg explores combinations with the rest of the elements.

Hence, in [2,3,6,7] the combination [2,2,3] which would be explored under the node exploring 2 would never be explored as [3,2,2] under the node exploring 3.

### Complexity
N = No. of elements, T = Target, M = Min. value in candidates

#### Time - O(2^T/M)
Exponential, since at each node we explore 2 more nodes and the max depth like this could be Target / Minimum Value (left most leg).

#### Space - O(T/M)
Space Complexity consists of 2 components - Recursive Stack & the List of combinations at each recursive call.

In the worst case, both can grow up to Target / Min. value (left most leg).
This grows linearly with the terget and min. candidate value.
