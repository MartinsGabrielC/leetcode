from ValidAnagram import SolutionValidAnagram

def main():
    solution = SolutionValidAnagram()
    assert(solution.isAnagramSorted("anagram","nagaram"))
    assert(solution.isAnagramCounter("anagram","nagaram"))
    assert(solution.isAnagramAdHoc("anagram","nagaram"))
    assert(not solution.isAnagramSorted("rat","car"))
    assert(not solution.isAnagramCounter("rat","car"))
    assert(not solution.isAnagramAdHoc("rat","car"))

if __name__ == "__main__":
    main()