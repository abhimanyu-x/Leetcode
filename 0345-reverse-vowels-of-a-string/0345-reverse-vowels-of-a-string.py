class Solution:
    def reverseVowels(self, s: str) -> str:
        vow="AEIOUaeiou"
        v=[]
        for i in s:
            if i in vow:
                v.append(i)

        k=v[::-1]
        x=0
        c=[]
        for i in s:
            if i in vow:
                c.append(k[x])
                x+=1
            else:
                c.append(i)

        return "".join(c)