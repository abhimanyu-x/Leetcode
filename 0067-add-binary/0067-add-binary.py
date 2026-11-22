class Solution:
    def addBinary(self, a: str, b: str) -> str:
        na=nb=0

        na=int(a,2)
        nb=int(b,2)

        k=na+nb

        return bin(k)[2:]
    