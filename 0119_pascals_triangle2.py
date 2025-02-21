from typing import List
from pprint import pprint

class Solution:
    def generate(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(1, rowIndex + 1):
            row = [1] + [row[j] + row[j + 1] for j in range(i - 1)] + [1]
        return row
    

if __name__ == '__main__':
    s = Solution()

    for i in range(10):
        print(s.generate(i))