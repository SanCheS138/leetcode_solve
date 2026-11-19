class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        path = []

        def backtrack(start: int) -> None:
            if len(path) == k:
                res.append(path.copy())
                return

            # Prune branches where not enough numbers remain to reach size k:
            # need (k - len(path)) more elements, so max start index is:
            # n - (k - len(path)) + 1
            upper = n - (k - len(path)) + 1
            for i in range(start, upper + 1):
                path.append(i)
                backtrack(i + 1)
                path.pop()

        backtrack(1)
        return res