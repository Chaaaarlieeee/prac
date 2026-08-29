class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for i,j in enumerate(nums):
            if target-j in hashtable:
                return [hashtable[target-j],i]
            else:
                hashtable[j]=i