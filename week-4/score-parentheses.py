class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        parens = list(S)
        track = [0]
        for c in parens:
            if c == '(':
                track.append(0)
            else:
                back = track.pop()
                track[-1] += 2 * back or 1
        return track.pop()