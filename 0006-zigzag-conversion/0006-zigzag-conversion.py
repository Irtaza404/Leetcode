class Solution:
    def convert(self,s, numRows):
        if numRows == 1:
            return s
        buckets = [""] * numRows
        current_row = 0
        direction = -1
        print(buckets)
        for char in s:
            if current_row >= numRows - 1:
                direction = 1
            elif current_row == 0:
                direction = -1

            buckets[current_row] += char

            if direction == -1:
                current_row += 1
            else:
                current_row -= 1
        print(buckets)
        return "".join(buckets)