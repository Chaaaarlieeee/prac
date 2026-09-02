class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashtable={}
        temp=[]
        for i,j in enumerate(s):
            if j not in hashtable:
                hashtable[j]=i
                temp.append(j)
            elif j in hashtable and j in temp:
                temp.remove(j)
        if not temp:
            return -1
        else: return hashtable[temp[0]]


class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashtable={}
        for i in s:
            if i not in hashtable:
                hashtable[i]=1
            else:
                hashtable[i]+=1
        k=0
        for i in s:
            if hashtable[i]==1:
                return k
            else: k+=1
        return -1