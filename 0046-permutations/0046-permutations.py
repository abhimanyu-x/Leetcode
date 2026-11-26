from itertools import permutations
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        k=list(permutations(nums,len(nums)))

        return k
