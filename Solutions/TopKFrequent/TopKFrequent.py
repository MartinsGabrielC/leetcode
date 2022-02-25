from collections import Counter
from typing import List
class SolutionTopKFrequent:
    def topKFrequentCounter(self, nums: List[int], k: int) -> List[int]:
        numCounter = Counter(nums)
        mostFrequent = numCounter.most_common(k)
        return [item[0] for item in mostFrequent]
    
    def topKFrequentAdHoc(self, nums: List[int], k: int) -> List[int]:
        numCounter = {}
        for num in nums:
            if num in numCounter:
                numCounter[num] += 1
            else:
                numCounter[num] = 1
        sortedDict = dict(reversed(sorted(numCounter.items(), key=lambda item: item[1])))
        return [item[0] for item in list(sortedDict.items())[:k]]

