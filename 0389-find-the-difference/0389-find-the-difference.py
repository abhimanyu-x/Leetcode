class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        mp1={}
        for i in s:
            if i not in mp1:
                mp1[i]=s.count(i)

        mp2={}
        for j in t:
            if j not in mp2:
                mp2[j]=t.count(j)

        for k in mp2:
            if k not in mp1 or mp2[k]>mp1[k]:
                return k


