class Solution:
    def isValid(self, s: str) -> bool:
        validate = []
        length = len(s)
        if not s:
            return True
        
        if length == 1:
            return False

        for c in s[::-1]:
            if c == ')':
                validate.append('(')
            elif c == ']':
                validate.append('[')
            elif c == '}':
                validate.append('{')
            else:
                try:
                    check = validate.pop()
                except IndexError:
                    return False
                
                if c == '(' and check != '(': return False
                elif c == '[' and check != '[': return False
                elif c == '{' and check != '{': return False
        
        if len(validate) > 0:
            return False
        
        return True