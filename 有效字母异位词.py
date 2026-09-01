class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        i={}
        for k in s:
            if k not in i:
                i[k]=1
            else:
                i[k]+=1

        for l in t:
            if l not in i:
                return False
            elif i[l]==0:
                return False
            else: i[l]-=1
        return True
    
a=Solution()
a.isAnagram(s = "anagram", t = "nagaram")
