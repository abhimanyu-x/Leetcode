class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z=nums.count(0)
        o=nums.count(1)
        t=nums.count(2)
        for i in range(z):
            nums[i]=0
        for j in range(z,o+z):
            nums[j]=1
        for k in range(z+o,len(nums)):
            nums[k]=2

            
