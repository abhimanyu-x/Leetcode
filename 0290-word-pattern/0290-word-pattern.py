class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        x=s.split()
        if len(pattern)!=len(x):
            return False
        m={}
        fl=0
        for i in range(len(pattern)):
            if pattern[i] not in m and x[i] in m.values():
                fl=1
                break
            if pattern[i] not in m:
                m[pattern[i]]=x[i]
            else:
                if x[i]!=m[pattern[i]]:
                    fl=1
                    break

        if fl==0:
            return True
        else:
            return False
                