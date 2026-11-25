from functools import cmp_to_key
class Solution:
    def compare(self,a,b):
        if a+b>b+a:
            return -1
        elif b+a>a+b:
            return 1
        else:
            return 0
    def largestNumber(self, nums: list[int]) -> str:
        k=[]
        for i in nums:
            k.append(str(i))
        k.sort(key=cmp_to_key(self.compare))

        if k[0]=="0":
            return "0"
        else:
            return "".join(k)
        
