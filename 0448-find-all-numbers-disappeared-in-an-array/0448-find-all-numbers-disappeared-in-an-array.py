class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        k=[]
        s=set(nums)
        for i in range(1,len(nums)+1):
            if i not in s:
                k.append(i)

        return k