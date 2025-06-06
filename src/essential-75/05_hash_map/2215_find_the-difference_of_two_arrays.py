class Solution:
    def findDifference(self, nums1, nums2):
        s1, s2 = set(nums1), set(nums2)
        ans = [[], []]

        for i in s1:
            if i not in s2:
                ans[0].append(i)
        
        for i in s2:
            if i not in s1:
                ans[1].append(i)
        
        return ans
    


    # class Solution:
    # def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
    #     nums1Map = {}
    #     nums2Map = {}

    #     for n in nums1:
    #         if n not in nums1Map:
    #             nums1Map[n] = 1

    #     for n in nums2:
    #         if n not in nums2Map:
    #             nums2Map[n] = 1


        
    #     nums1Diff = []
    #     for n2 in nums2:
    #         if n2 not in nums1Map:
    #             nums1Diff.append(n2)
    #             nums2Map[n2] = 1
                
    #     nums2Diff = []
    #     for n1 in nums1:
    #         if n1 not in nums2Map:
    #             nums2Diff.append(n1)
    #             nums2Map[n1] = 1


    #     return [nums2Diff, nums1Diff]