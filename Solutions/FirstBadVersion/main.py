from FirstBadVersion import SolutionFirstBadVersion

def main():
    solution = SolutionFirstBadVersion(5)
    assert(solution.firstBadVersion(10) == 5 )
    assert(solution.firstBadVersion(5) == 5 )
    solution2 = SolutionFirstBadVersion(2)
    assert(solution2.firstBadVersion(10) == 2 )
    assert(solution2.firstBadVersion(5) == 2 )

if __name__ == "__main__":
    main()