class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        n = len(nums)
        lsum = 0
        rsum = sum(nums[1:])
        pivot = 0
        
        if rsum == 0:
            return 0
        else:
            rsum -= nums[1]
        
        for i in range(1, n-1):
         
            lsum += nums[i-1]        
            if lsum == rsum:
                return i
            else:
                rsum -= nums[i+1]
      
        if sum(nums[:-1]) == 0:
            return n-1

        return -1