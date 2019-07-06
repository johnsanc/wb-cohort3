class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        letters = list("abcdefghijklmnopqrstuvwxyz")
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        mappings = {}
        
        for key, val in zip(letters, morse):
            mappings[key] = val
        
        transformations = []
        for word in words:
            t_word  = ""
            for letter in word:
                t_word += mappings[letter]
            transformations.append(t_word)
        
        return len(set(transformations))