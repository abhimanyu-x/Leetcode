class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sentence.strip()
        x=sentence.split()
        s=""
        for i in range(len(x)):
            if x[i][0] in "AEIOUaeiou":
                s+=x[i]+"ma"+("a"*(i+1))+" "
            elif x[i][0] not in "AEIOUaeiou":
                if len(x[i])==1:
                    s+=x[i]+"ma"+("a"*(i+1))+" "
                else:
                    s+=x[i][1::]+x[i][0]+"ma"+("a"*(i+1))+" "

        return s.strip()