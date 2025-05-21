""" 283. Move Zeros

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the
non-zero elements.

Note that you must do this in-place without making a copy of the array.


Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
    1 <= nums.length <= 104
    -231 <= nums[i] <= 231 - 1

Follow up: Could you minimize the total number of operations done?
"""

# 2025/05/20
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 1
        n = len(nums)

        while j < n:
            if nums[i] == 0:
                while nums[j] == 0:
                    j += 1
                    if j == n:
                        return

                nums[i], nums[j] = nums[j], 0
            i += 1
            j += 1