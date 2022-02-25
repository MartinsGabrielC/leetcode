from typing import List
class LetterCombinationSolution:
    def combine(self, result: List[str], digit:int) -> List[str]:
        digitMap = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        if ( len(result) == 0 ) :
            return [letter for letter in digitMap[digit]]
        retVal = []
        for entry in result:
            for letter in digitMap[digit]:
                retVal.append(entry+letter)
        return retVal
                
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        for digit in digits:
            result = self.combine(result,digit)
        return result