class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper():
            return True
        elif word.islower():
            return True
        else:
            if word[0].isupper() and word[1:].islower():
                return True
            else:
                return False