from util.tests import run_test_case\

class Solution:
    '''
    Note to self: Dict lookups are expensive. 
    '''

    roman_to_int = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    roman_to_int_tuples = [
        ("M", 1000),
        ("D", 500),
        ("C", 100),
        ("L", 50),
        ("X", 10),
        ("V", 5),
        ("I", 1)
    ]

    def romanToIntReversed(self, s: str) -> int:
        
        int_val = 0
        prev_val = 0
        # Reverse the string to make it easier to handle subtraction cases
        for c in s[::-1]:
            val = self.roman_to_int[c]
            if val < prev_val:
                int_val -= val
            else:
                int_val += val
            prev_val = val
        return int_val
    
    def romanToIntNoReverse(self, s: str) -> int:
        int_val = 0
        prev_val = 0
        for c in s:
            val = self.roman_to_int[c]
            if val > prev_val:
                int_val -= prev_val
            else:
                int_val += prev_val
            prev_val = val

        # Add the last letter
        int_val += prev_val

        return int_val

    
    def romanToInt(self, s: str) -> int:
        return self.romanToIntReversed(s)


if __name__ == "__main__":
    s = Solution()
    run_test_case(s.romanToInt, ("III",), 3)
    run_test_case(s.romanToInt, ("IV",), 4)
    run_test_case(s.romanToInt, ("IX",), 9)
    run_test_case(s.romanToInt, ("LVIII",), 58)
    run_test_case(s.romanToInt, ("MCMXCIV",), 1994)
    run_test_case(s.romanToInt, ("I",), 1)
    run_test_case(s.romanToInt, ("II",), 2)
    run_test_case(s.romanToInt, ("V",), 5)
    run_test_case(s.romanToInt, ("X",), 10)
    run_test_case(s.romanToInt, ("L",), 50)
    run_test_case(s.romanToInt, ("C",), 100)
    run_test_case(s.romanToInt, ("D",), 500)
    run_test_case(s.romanToInt, ("M",), 1000)
    run_test_case(s.romanToInt, ("MM",), 2000)
    run_test_case(s.romanToInt, ("MMM",), 3000)
    run_test_case(s.romanToInt, ("MMMM",), 4000)
    run_test_case(s.romanToInt, ("MMMCM",), 3900)