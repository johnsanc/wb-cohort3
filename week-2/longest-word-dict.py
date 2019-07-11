class Solution:
    def longestWord(self, words: List[str]) -> str:
        prefix = set()
        
        for word in words:
            builder = ""
            for l in word:
                builder += l
                if len(builder) > 1 and builder in words and builder[:-1] in prefix:
                    prefix.add(builder)
                elif len(builder) == 1 and builder in words:
                    prefix.add(builder)
        
        sort_set = sorted(prefix, reverse=True, key=len)
        longest_len = len(sort_set[0])
        longest_word = sort_set[0]
        
        for i in range(1, len(sort_set)):
            if len(sort_set[i]) == longest_len and sort_set[i] < longest_word:
                longest_word = sort_set[i]
                
        return longest_word

if __name__ == "__main__":
    sol = Solution()
    result = sol.longestWord(["a","banana","app","appl","ap","apply","apple"])
    print(result)