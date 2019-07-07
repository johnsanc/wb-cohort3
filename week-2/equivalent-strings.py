class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        return len(set("".join(sorted(string[0::2])) + "".join(sorted(string[1::2])) for string in A))