class Solution:
    def reverseWords(self, s: str) -> str:
        l=0
        r=0
        i=len(s)-1
        if i==0:
            return s
        sw=""
        while i>0:
            while i>=0 and s[i]==" ":
                i-=1
            r=i
            while i>=0 and s[i]!=" ":
                i-=1
            l=i
            sw=sw+s[l+1:r+1]+" "
        return sw.strip()