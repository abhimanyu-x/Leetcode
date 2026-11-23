class Solution:
    def reverseWords(self, s: str) -> str:
        x=s.split()
        s=str()
        for i in x:
            s=s+i[::-1]+" "

        return s.strip()