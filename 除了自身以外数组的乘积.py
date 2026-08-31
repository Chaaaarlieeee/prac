class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer = [1] * len(nums)
        left=1
        l=0
        while l<len(nums):
            answer[l]=left
            left*=nums[l]
            l+=1
            
        right=1
        r=len(nums)-1
        while r>-1:
            answer[r]*=right
            right*=nums[r]
            r-=1

