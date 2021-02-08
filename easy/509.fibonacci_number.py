class Solution:
    # naive way, O(2^N) time, O(N) space
    def recursive_fib(self, N):
        if N < 2:
            return N
        return self.recursive_fib(N - 1) + self.recursive_fib(N - 2)

    # memoization recursive, O(N) time, O(N) space
    def fib_memo_rec(self, n: int, memo: dict) -> int:
        if n == 0:
            return 0
        elif n <= 2:
            return 1
        elif n in memo:
            return memo[n]
        m = self.fib_memo_rec(n - 1, memo) + self.fib_memo_rec(n - 2, memo)
        memo[n] = m
        return m

    # top-down, O(N) time, O(1) space
    def fib_memo(self, n: int) -> int:
        if n == 0:
            return 0
        elif n <= 2:
            return 1
        minus_1 = 1
        minus_2 = 1
        for x in range(n - 1):
            minus_2, minus_1 = minus_1, minus_1 + minus_2
        return minus_2
