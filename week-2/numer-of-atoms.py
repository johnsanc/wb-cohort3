from collections import defaultdict
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        elements = defaultdict(int)
        stack = []
        atom = ""
        count, mult_factor, i = 0, 1, 0
        
        for char in formula[::-1]:
            if char.isdigit():
                count += int(char) * 10**i #adds the tens/hundreds/etc place if num is > 9
                i += 1
            elif char == ')':
                mult_factor *= count
                stack.append(count)
                count = i = 0
            elif char == '(':
                mult_factor //= stack.pop()
                count = i = 0
            elif char.islower():
                atom += char
            elif char.isupper():
                atom += char
                elements[atom[::-1]] += (count or 1) * mult_factor
                atom = ""
                count = i = 0
        
        return "".join(atom + str(count > 1 and count or "") for atom,count in sorted(elements.items()))
                