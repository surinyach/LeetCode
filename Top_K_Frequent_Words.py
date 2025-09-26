from collections import Counter

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        result = []
        freq = Counter(words)
        sorted_freq = sorted(freq.keys(), key= lambda w: (-freq[w], w))

        for i in range(0, k):
            result.append(sorted_freq[i])

        return result