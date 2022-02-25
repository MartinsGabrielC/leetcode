from typing import List
class SolutionLongestCommonPrefix:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if( len(strs) == 0 ):
            return ""
        else:
            sameLetter = True
            counter = 0
            result = ""
            while( sameLetter and counter < len(strs[0])):
                letter = strs[0][counter]
                for string in strs:
                    if( len(string) > counter ):
                        if ( string[counter] != letter):
                            sameLetter = False

                    else:
                        sameLetter = False
                if sameLetter:
                    result += letter
                    counter += 1
            return result