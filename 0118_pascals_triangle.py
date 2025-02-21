from typing import List
from pprint import pprint

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row)
        return triangle
    

if __name__ == '__main__':
    s = Solution()

    for i in range(10):
        pprint(s.generate(i))
        print()