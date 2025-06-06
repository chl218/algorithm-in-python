""" 1679. Max Number of K-Sum Pairs

You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

 
Example 1:
Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.


Example 2:
Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.


Constraints:
    1 <= nums.length <= 10^5
    1 <= nums[i] <= 10^9
    1 <= k <= 10^9
"""

# 2025/05/26
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        nums.sort()

        i, j = 0, len(nums)-1
        count = 0

        while i < j:
            ssum = nums[i] + nums[j]
            if ssum == k:
                count += 1
                i += 1
                j -= 1
            elif ssum > k:
                j -= 1
            else:
                i += 1
        
        return count
    


# class Solution:
#     def maxOperations(self, nums: List[int], k: int) -> int:
#         freq_map = {}
#         cnt = 0
#         for num in nums:
#             if freq_map.get(k - num, 0) > 0:
#                 freq_map[k - num] -= 1
#                 cnt += 1
#             else:
#                 freq_map[num] = freq_map.get(num, 0) + 1
#         return cnt