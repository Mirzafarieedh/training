class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


        if len(s) != len(t):
            return False
    
        counts, countT = {}, {}
    
    # Count characters in s
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
    
    # Subtract using t
            for c in counts:
                if countS[c] != countT.get(c, 0):
                   return False

            return True




        