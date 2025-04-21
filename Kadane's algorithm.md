# Kadane's algorithm

### Maximum subarray

[Maximum Subarray - Amazon Coding Interview Question - Leetcode 53 - Python - YouTube](https://www.youtube.com/watch?v=5WZl3MMT0Eg)

Given an integer array `nums`, find the subarray with the largest sum, and return *its sum*.

**Example 1:**

**Input:** nums = [-2,1,-3,4,-1,2,1,-5,4]
**Output:** 6
**Explanation:** The subarray [4,-1,2,1] has the largest sum 6.

**Example 2:**

**Input:** nums = [1]
**Output:** 1
**Explanation:** The subarray [1] has the largest sum 1.

**Example 3:**

**Input:** nums = [5,4,-1,7,8]
**Output:** 23
**Explanation:** The subarray [5,4,-1,7,8] has the largest sum 23.

#### Brute force:

```python
def maxSubArray(nums):
    n = len(nums)
    max_sum = 0

    for i in range(n):
        for j in range(i,n):
            insitu_sum = sum(nums[i:j+1])
            max_sum = max(max_sum, insitu_sum)

    return max_sum
```

## Kadane's algorithm

Here's how Kadane's algorithm works:

1. Initialization: Initialize two variables, `max_so_far` and `max_ending_here`, to the value of the first element in the array. We will use these variables to keep track of the maximum subarray sum found so far and the maximum sum ending at the current index.

2. Iteration: Start iterating through the array from the second element (index 1) to the last element.

3. For each element, do the following:
   
   a. Update `max_ending_here`: Add the current element to the `max_ending_here` variable. If the current element is greater than the sum of the current element and `max_ending_here`, update `max_ending_here` to the current element. This step is crucial as it helps in considering only contiguous subarrays.
   
   b. Update `max_so_far`: Compare `max_so_far` with the updated value of `max_ending_here`. If `max_ending_here` is greater than `max_so_far`, update `max_so_far` to `max_ending_here`. This step ensures that `max_so_far` always holds the maximum subarray sum found so far.

4. Continue the iteration until you reach the end of the array.

5. The result: At the end of the iteration, `max_so_far` will contain the maximum subarray sum in the given array.

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = 0

        for n in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += n

            max_sum = max(max_sum, curr_sum)

        return max_sum
```
