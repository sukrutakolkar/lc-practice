# 442. Find All Duplicates in an Array
**Difficulty** - Medium

**Topic(s)** - Array 

### Description
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.

You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, excluding the space needed to store the output

Example 1:

>Input: nums = [4,3,2,7,8,2,3,1]<br>
>Output: [2,3]
Example 2:

>Input: nums = [1,1,2]<br>
>Output: [1]
Example 3:

>Input: nums = [1]<br>
>Output: []

### Solution
```python
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
```

### Explanation: 
A hashmap or set could solve this easily but a key constraint is the constant space complexity.

All the elements are positive and are in the range 1 to n, where n = len(nums).

Hence, we use the indices as a map.

Each element e maps to an index e-1. We can then mark that value aas seen by negating its indexed value.
If we do this for all elements in the array, we can find duplicates by checking the indexed values for each element.

### Complexity

#### Time - O(N)

#### Space - O(1)
