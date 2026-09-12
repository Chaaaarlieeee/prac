class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1=len(word1)
        l2=len(word2)
        count=l1-l2
        end=""
        if count<0:
            end=word2[l2-abs(count):]
        elif count>0:
            end=word1[l1-count:]
        sw=""
        i,j=0,0
        while i<=l1-1 and j<=l2-1:
            sw+=word1[i]+word2[j]
            i+=1
            j+=1
        sw+=end
        return sw
