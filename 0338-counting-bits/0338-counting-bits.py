class Solution:
    def countBits(self, n: int) -> list[int]:
        ans=list()
        for i in range(0,n+1):
            k=0
            t=i
            while (t!=0):
                if t%2==1:
                    k+=1
                t=t//2
            ans.append(k)

        return ans
    