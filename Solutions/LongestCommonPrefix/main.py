from LongestCommonPrefix import SolutionLongestCommonPrefix

def main():
    solution = SolutionLongestCommonPrefix()
    assert(solution.longestCommonPrefix(["flower","flow","flight"]) == "fl" )
    assert(solution.longestCommonPrefix(["dog","racecar","car"]) == "" )
    assert(solution.longestCommonPrefix(["hello","hello world","hello team"]) == "hello" )

if __name__ == "__main__":
    main()