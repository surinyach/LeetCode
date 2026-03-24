class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        candidates = {}
        for i in range(0, len(numbers)):
            n = numbers[i]
            to_target = target - n
            if to_target in candidates.keys():
                return [candidates[to_target], i + 1]
            else:
                candidates[n] = i + 1