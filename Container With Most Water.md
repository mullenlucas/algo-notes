11. ## Container With Most Water

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `ith` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return *the maximum amount of water a container can store*.

**Notice** that you may not slant the container.

**Example 1:**

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg)

**Input:** height = [1,8,6,2,5,4,8,3,7]
**Output:** 49
**Explanation:** The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

**Example 2:**

**Input:** height = [1,1]
**Output:** 1

### Two-pointer strategy

1. Initialize two pointers, left and right, at the two ends of the array. Set left to 0 and right to n - 1, where n is the length of the input array.

2. Calculate the area formed by the two lines represented by the pointers (left and right). The area can be calculated as the minimum of the two line heights multiplied by the distance between them, i.e., `area = min(height[left], height[right]) * (right - left)`.

3. Move the pointer that points to the smaller height inward. If `height[left] < height[right]`, increment left by 1; otherwise, decrement right by 1.

4. Repeat steps 2 and 3 until the left pointer is less than the right pointer.

5. Keep track of the maximum area encountered during this process, and return it as the result.

The intuition behind the Two Pointer Approach is that if you move the pointer that points to the smaller height inward, it might lead to finding a greater area. This is because moving the pointer with the larger height inward will not improve the area, as the height of the container is limited by the smaller height.

## Solution

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        pl = 0
        pr = len(height)-1
        max_area = 0

        while pl < pr:
            # area rectng: b*h
            # b = pr - pl
            # h = min(height[pl], height[pr])
            area = (pr-pl) * min(height[pl], height[pr])
            max_area = max(max_area, area)

            # move the pointer that points to the smaller height inward
            # if left pointer < right pointer => move left inward
            if height[pl] < height[pr]
                pl += 1
            # else if right pointer < left pointer => move right inward
            else:
                pr -= 1

        return max_area
```
