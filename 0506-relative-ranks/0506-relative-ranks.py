class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        k=sorted(score,reverse=True)
        mp={}
        answer=[]
        if len(score)==1:
            return ["Gold Medal"]
        elif len(score)==2:
            if score[0]>score[1]:
                return ["Gold Medal","Silver Medal"]
            else:
                return ["Silver Medal","Gold Medal"]
        elif len(score) == 3:
            if score[0] > score[1] and score[1] > score[2]:
                return ["Gold Medal", "Silver Medal", "Bronze Medal"]

            elif score[1] > score[0] and score[0] > score[2]:
                return ["Silver Medal", "Gold Medal", "Bronze Medal"]

            elif score[0] > score[2] and score[2] > score[1]:
                return ["Gold Medal", "Bronze Medal", "Silver Medal"]

            elif score[1] > score[2] and score[2] > score[0]:
                return ["Bronze Medal", "Gold Medal", "Silver Medal"]

            elif score[2] > score[0] and score[0] > score[1]:
                return ["Silver Medal", "Bronze Medal", "Gold Medal"]

            elif score[2] > score[1] and score[1] > score[0]:
                return ["Bronze Medal", "Silver Medal", "Gold Medal"]

        else:
            mp[k[0]]="Gold Medal"
            mp[k[1]]="Silver Medal"
            mp[k[2]]="Bronze Medal"

            for i in range(3,len(k)):
                mp[k[i]]=str(i+1)

            for i in score:
                if i in mp:
                    answer.append(mp[i])

        return answer