class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        ssum = sum(nums[0:k])
        avg = ssum / k
        
        for i in range(1, len(nums)-k+1):
            ssum = ssum - nums[i-1] + nums[i+k-1]
            tmp_avg = ssum / k
            
            if tmp_avg > avg:
                avg = tmp_avg

        return avg