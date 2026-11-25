class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        k = strs.copy()

        for i in range(len(k)):
            k[i] = "".join(sorted(k[i]))

        mp = {}

        for i in range(len(k)):
            if k[i] not in mp:
                mp[k[i]] = []
            mp[k[i]].append(i)

        out = []

        for i in mp.values():
            temp = []
            for j in i:
                temp.append(strs[j])
            out.append(temp)

        return out