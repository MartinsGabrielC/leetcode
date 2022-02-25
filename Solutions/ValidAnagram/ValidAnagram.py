from collections import Counter

class SolutionValidAnagram:
    def isAnagramSorted(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
    
    def isAnagramCounter(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    
    def isAnagramAdHoc(self, s: str, t: str) -> bool:
        if ( len(s) == len(t) ):
            sCounter = {}
            tCounter = {}
            for letter in s:
                if letter in sCounter:
                    sCounter[letter] += 1
                else:
                    sCounter[letter] = 1
            for letter in t:
                if letter in tCounter:
                    tCounter[letter] += 1
                else:
                    tCounter[letter] = 1
            return sCounter == tCounter
        else:
            return False

