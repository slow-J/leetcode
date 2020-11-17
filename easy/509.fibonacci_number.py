class Solution:
    # def fib(self, N: int) -> int:
    def recursive_fib(self, N):
        if N < 2:
            return N
        return self.recursive_fib(N - 1) + self.recursive_fib(N - 2)
