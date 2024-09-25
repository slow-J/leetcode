from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for txt in strs:
            lex_srt = str(sorted(txt))
            anagrams[lex_srt].append(txt)

        return anagrams.values()
