class Solution:
    def convert(self, s: str, numRows: int) -> str:
        return zigzag_conversion(s, numRows)

def zigzag_conversion(s, numRows):
    #iterate across characters in string
    #one pointer for the row
    #add character from string to a row in zig zag order
    #return the joined string
    #time complexity O(n)
    #space complexity O(n)
    row_p = 0
    prev_p = -1
    rows = {}
    final_string = ""
    if numRows == 1:
        return s
    for char in s:
        if rows.get(row_p):
            temp = rows.get(row_p)
            temp.append(char)
            rows[row_p] = temp
        else:
            rows[row_p] = [char]
        if row_p == numRows-1:
            prev_p = row_p
            row_p -= 1
        elif row_p == 0:
            prev_p = row_p
            row_p += 1
        elif prev_p > row_p:
            prev_p = row_p
            row_p -= 1
        elif prev_p < row_p:
            prev_p = row_p
            row_p += 1
    for key in rows:
        final_string += "".join(rows.get(key))
    return final_string