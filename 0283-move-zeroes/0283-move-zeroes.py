class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos=0
        k=0
        for i in range(len(nums)):
            if nums[i]==0:
                k=i
                break
        if k == 0 and 0 not in nums:
            return
        for i in range(1,len(nums)):
            if nums[i-1]==0 and nums[i]!=0:
                t=nums[k]
                nums[k]=nums[i]
                nums[i]=t 
                k+=1

        
        
