class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        counts = defaultdict(int)
        
        for num in nums:
            counts[num] += 1
                    
        for k, v in counts.items():
            if v == 1:
                return k
            
        return -1