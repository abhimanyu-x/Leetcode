class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        c=0
        k=[]
        for i in nums:
            if i==1:
                c+=1
                k.append(c)
            else:
                c=0
        if not k:
            return 0
        return max(k)