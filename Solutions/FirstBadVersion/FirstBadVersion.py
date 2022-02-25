class SolutionFirstBadVersion:
    def __init__(self, bad: int):
        self.badVersion = bad
    
    def isBadVersion(self, version: int):
        return version >= self.badVersion

    def firstBadVersion(self, n: int) -> int:
        if( n == 1 ):
            return n
        start = 1
        end = n
        while( start <= end ):
            middle = (start+end)//2
            if( self.isBadVersion(middle) and not self.isBadVersion(middle-1) ):
                return middle
            elif( self.isBadVersion(middle - 1) ):
                end = middle - 1
            else:
                start = middle + 1

