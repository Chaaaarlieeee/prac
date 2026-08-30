class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=len(nums)
        slow,fast=1,1
        while fast<l:
            if nums[fast]!=nums[fast-1]:
                nums[slow]=nums[fast]
                slow+=1
            fast+=1
        return slow