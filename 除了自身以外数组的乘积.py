class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        answer = [1] * len(nums)
        left=1
        l=0
        for i in range(len(nums)):
            answer[i]=left
            left*=nums[i]
        right=1
        r=len(nums)-1
        while r>-1:
            answer[r]*=right
            right*=nums[r]
            r-=1

