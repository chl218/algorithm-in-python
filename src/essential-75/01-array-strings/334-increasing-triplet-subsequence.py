""" 334. Increasing Triplet Subsequence

Given an integer array nums, return true if there exists a triple of indices
(i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such
indices exists, return false.

"""
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        first, second = float('inf'), float('inf')  

        i = 0
        while i < len(nums):
            num = nums[i]
            
            if num <= first:
                first = num  
            elif num <= second:
                second = num 
            else:
                return True
            
            i += 1  
        
        return False
