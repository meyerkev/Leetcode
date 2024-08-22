from util.tests import run_test_case
class Solution:
    match = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in self.match:
                # Popping an empty stack will throw an error
                if not stack or not self.match[c] == stack.pop():
                    return False
            else:
                stack.append(c)
        return not stack
    

if __name__ == "__main__":
    s = Solution()
            
    run_test_case(s.isValid, ("()",), True)
    run_test_case(s.isValid, ("()[]{}",), True)
    run_test_case(s.isValid, ("(]",), False)
    run_test_case(s.isValid, ("([)]",), False)
    run_test_case(s.isValid, ("{[]}",), True)
    run_test_case(s.isValid, ("",), True)
    run_test_case(s.isValid, ("[",), False)
    run_test_case(s.isValid, ("]",), False)
    run_test_case(s.isValid, ("[(",), False)
    run_test_case(s.isValid, ("[)",), False)
