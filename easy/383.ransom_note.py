class Solution:
    # def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    def canConstruct(ransomNote, magazine):
        letters_dict = dict()
        for letter in magazine:
            if letter in letters_dict:
                letters_dict[letter] = letters_dict[letter] + 1
            else:
                letters_dict[letter] = 1

        for letter in ransomNote:
            if letter in letters_dict:
                if letters_dict[letter] > 0:
                    letters_dict[letter] = letters_dict[letter] - 1
                else:
                    return False
            else:
                return False

        return True
