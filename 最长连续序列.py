class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num=set(nums)
        max_len=0
        length=1
        if not nums:
            return 0
        for i in num:
            if i-1 not in num:
                length=1
                while i+1 in num:
                    i+=1
                    length+=1
                max_len=max(max_len,length)
        return max_len
