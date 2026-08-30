class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1 or len(nums) == 2:
            return nums[0]
        hashtable={}
        for i,j in enumerate(nums):
            if j in hashtable:
                hashtable[j]+=1
            else:hashtable[j]=1
            if hashtable[j]>len(nums)/2:
                return j
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate=None
        count=0
        for num in nums:
            if count==0:
                candidate=num
            count+=1 if nums==candidate else count-=1
        return candidate