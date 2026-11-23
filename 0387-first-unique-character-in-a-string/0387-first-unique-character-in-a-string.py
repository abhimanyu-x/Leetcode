class Solution:
    def firstUniqChar(self, s: str) -> int:
        mp={}
        for i in range(len(s)):
            if s[i] not in mp:
                mp[s[i]]=1
            else:
                mp[s[i]]+=1
        k=0
        fl=0
        for i in mp:
            if mp[i]==1:
                fl=1
                k=s.index(i)
                break
        if fl==1:
            return k
        else:
            return -1
        
            

        
        
            