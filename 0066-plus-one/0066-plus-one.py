class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        s=0
        for i in digits:
            s=s*10+i
        s=s+1

        t=s
        k=list()
        while (t!=0):
            d=t%10
            k.append(d)
            t=t//10

        return k[::-1]
        