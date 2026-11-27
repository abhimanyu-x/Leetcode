class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c=0
        a=sorted(ransomNote)
        b=sorted(magazine)
        for i in a:
            if i in b:
                c+=1
                b.remove(i)

        if c==len(ransomNote):
            return True
        else:
            return False
        
                