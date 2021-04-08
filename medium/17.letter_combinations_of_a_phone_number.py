class Solution:
    # https://stackoverflow.com/questions/5125619/why-doesnt-list-have-safe-get-method-like-dictionary
    def safe_list_get(self, l, idx, default):
        try:
            return l[idx]
        except IndexError:
            return default

    def letterCombinations(self, digits: str) -> List[str]:
        """Bruteforce. Recursive backtracking might be quicker but the constraint is tiny: 0 <= digits.length <= 4
        so brute force is sufficient.
        Runtime: 28 ms, faster than 81.79%
        Memory Usage: 14.1 MB, less than 86.13%
        """
        translation = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
            "-1": [],
        }
        permutations = []

        one = translation[self.safe_list_get(digits, 0, "-1")]
        if len(digits) == 1:
            return one
        two = translation[self.safe_list_get(digits, 1, "-1")]
        three = translation[self.safe_list_get(digits, 2, "-1")]
        four = translation[self.safe_list_get(digits, 3, "-1")]

        for onedig in one:
            if two:
                for twodig in two:
                    if three:
                        for threedig in three:
                            if four:
                                for fourdig in four:
                                    permutations.append(
                                        onedig + twodig + threedig + fourdig
                                    )
                            else:
                                permutations.append(onedig + twodig + threedig)
                    else:
                        permutations.append(onedig + twodig)
            else:
                permutations.append(onedig)

        return permutations
