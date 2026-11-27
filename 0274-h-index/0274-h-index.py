class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort()
        k=[]
        for i in range(len(citations)):
            if citations[i]>=len(citations[i::]):
                k.append(len(citations[i::]))

        if not k:
            return 0
        return max(k)   