class Solution:
    def findComplement(self, num: int) -> int:
        mask = 1
        while mask <= num:
            mask = 2 * mask
        mask -= 1

        return num ^ mask

