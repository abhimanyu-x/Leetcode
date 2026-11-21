class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        s=0
        a=str()
        fl=1
        for j in range(len(strs[0])):
            if fl==0:
                break
            s=0
            for i in range(len(strs)):
                if j>=len(strs[i]):
                    fl=0
                    break
                if strs[i][j]==strs[0][j] :
                    s+=1
                else:
                    fl=0
                    break
            
            if s==len(strs):
                a=a+strs[0][j]
        return a