class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            a=str()
            t=[]
            for i in range(len(s)-len(s)%k):
                a+=s[i]
                if i%k==k-1:
                    t.append(a)
                    a=""
            if len(s)%k!=0:
                t.append(s[len(s)-len(s)%k:len(s)])
            print(t)
            s=""
            for i in t:
                f=int(i)
                c=0
                while f!=0:
                    d=f%10
                    c+=d
                    f=f//10
                s+=str(c)
        return s