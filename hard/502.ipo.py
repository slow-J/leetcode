from heapq import nlargest


class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        # Quite slow without this 2-line hack/optimisation
        if W >= max(Capital):
            return W + sum(nlargest(k, Profits))

        zipped = zip(Capital, Profits)
        zipped = sorted(zipped, key=lambda tup: tup[1])[::-1]
        while k >= 1:
            for tup in zipped:
                if tup[0] <= W:
                    W += tup[1]
                    zipped.remove(tup)
                    break
            k -= 1
        return W
