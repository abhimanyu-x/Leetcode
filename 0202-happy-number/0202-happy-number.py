class Solution:
    def isHappy(self, n: int) -> bool:
        fl=1
        seen=set()
        while(fl==1):
            t=n
            s=0
            while(t!=0):
                d=t%10
                s+=pow(d,2)
                t=t//10
            n=s
            if n in seen:
                return False
            seen.add(n)
            
            if n==1:
                fl=0
        if fl==0:
            return True
        else:
            return False
        


