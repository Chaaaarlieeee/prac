class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:]=nums2
        nums1.sort()
        return nums1
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        sort=[]
        p1,p2=0,0
        while p1 < m or p2 < n:
            if p1 == m:
                sort.append(nums2[p2])
                p2+=1
            elif p2 == n:
                sort.append(nums1[p1])
                p1+=1
            elif nums1[p1]<nums2[p2]:
                sort.append(nums1[p1])
                p1+=1
            else:
                sort.append(nums2[p2])
                p2+=1
        nums1[:]=sort
        return nums1

