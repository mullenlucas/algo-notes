169. ## Majority Element

Given an array `nums` of size `n`, return *the majority element*.

The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

**Example 1:**

**Input:** nums = [3,2,3]
**Output:** 3

**Example 2:**

**Input:** nums = [2,2,1,1,1,2,2]
**Output:** 2

## Explanation

### Using hash_map

Create a hashmap that stores how many time a key appears

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = {}

        for n in nums:
            if n in hash:
                hash[n] += 1
            else:
                hash[n] = 1

        # Using lambda function and the key parameter of the `max` function
        # It calculates the maximum value of hash, 
        # and the key parameter is equal to that max value
        max_key = max(hash, key=lambda k: hash[k])

        return max_key
```

## Booyer-Moore algorithm

```cmd
D:\ecademia\Complete Data Structures and Algorithms Software Interviews\3 - Lists & Arrays\19 - Boyer Moore.mp4
```

Minute: 9.36

The Boyer-Moore Voting Algorithm is a smart and efficient algorithm used to find the majority element in an array. The majority element is defined as the element that appears more than ⌊n / 2⌋ times in an array of size `n`, where ⌊x⌋ represents the floor function (rounds x down to the nearest integer).

The key idea behind the algorithm is to cancel out pairs of elements that are different and maintain the majority element if it exists. Since the majority element occurs more than ⌊n / 2⌋ times, any other element will not be able to cancel it out.

Here's how the algorithm works:

1. Initialize two variables, `candidate` and `count`, to keep track of the potential majority element and its count, respectively. Initially, set `candidate` to `None` and `count` to `0`.

2. Iterate through the array. For each element `num`, do the following:
   
   a. If `count` is `0`, it means we don't currently have a potential majority element. So, we set the current element `num` as the potential majority element by updating `candidate = num` and initialize the count to `1`.
   
   b. If the current element `num` is the same as the `candidate`, increment the `count`.
   
   c. If the current element `num` is different from the `candidate`, decrement the `count`.

3. After the iteration, the `candidate` will hold the potential majority element. However, there is one final step to verify if it indeed is the majority element.

4. Iterate through the array again and count the occurrences of the `candidate`. If the count of `candidate` is greater than ⌊n / 2⌋, then it is the majority element. Otherwise, the array doesn't have a majority element.

The reason this algorithm works is that the majority element, if it exists, will eventually survive the cancellation process and remain in the `candidate` variable with a count greater than zero. All other elements will have a net count of zero or negative. Since the majority element appears more than ⌊n / 2⌋ times, it will always win in the end.

The Boyer-Moore Voting Algorithm runs in linear time, making it an efficient solution for finding the majority element, and it uses constant space, which is an advantage over the hash map approach.

```python
def majority_element(nums):
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif candidate == num:
            count += 1
        else:
            count -= 1

    return candidate

# Example usage:
nums = [2, 2, 1, 1, 1, 2, 2]
result = majority_element(nums)
print(result)  # Output: 2

```


