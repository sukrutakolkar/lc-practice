# 300. Longest Increasing Subsequence
**Difficulty** - Medium

**Topic(s)** - Array 

### Description
Given an integer array nums, return the length of the longest strictly increasing 
subsequence.

Example 1:

>Input: nums = [10,9,2,5,3,7,101,18]<br>
>Output: 4
Example 2:

>Input: nums = [0,1,0,3,2,3]<br>
>Output: 4
Example 3:

>Input: nums = [7,7,7,7,7,7]<br>
>Output: 1

## Constraints
1 <= nums.length <= 2500<br>
-104 <= nums[i] <= 104

### Solution
```python
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
            
        return len(res)
```

### Explanation: 
For each number in the input array, check if there's any number greater than the given number. Replace the number if if it exists in the result array, if not, add the current number to the result array.
Since the result array is sorted, we can simply scan from left to right.   

While this runs in `N^2` time complexity simply replacing the linear scan to search for the number in result for a bigger than current number will reduce it to `N.logN`.

### Complexity

#### Time - O(N^2) or O(N logN) if using Binary Search 

#### Space - O(N)
