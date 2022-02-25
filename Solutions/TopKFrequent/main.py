from TopKFrequent import SolutionTopKFrequent

def main():
    solution = SolutionTopKFrequent()
    assert(solution.topKFrequentCounter([1,1,1,2,2,3],2) == [1,2])
    assert(solution.topKFrequentCounter([1],1) == [1])
    assert(solution.topKFrequentAdHoc([1,1,1,2,2,3],2) == [1,2])
    assert(solution.topKFrequentAdHoc([1],1) == [1])

if __name__ == "__main__":
    main()