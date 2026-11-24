import math 
class Solution:
    def prodeq(self, a):
        prod=1
        for i in a:
            prod*=i

        gc=math.gcd(*a)
        lc=math.lcm(*a)

        if prod==gc*lc:
            return True
        else:
            return False
    
    def maxLength(self, nums: List[int]) -> int:
        k=[]
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if self.prodeq(nums[i:j+1]):
                   k.append(nums[i:j+1])
        max=0
        for i in k:
            if len(i)>max:
                max=len(i)

        return max

