class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        if len(nums)<2:
            return 0

        nums.sort()
        max=0
        for i in range(1,len(nums)):
            if nums[i]-nums[i-1]>max:
                max=nums[i]-nums[i-1]

        return max