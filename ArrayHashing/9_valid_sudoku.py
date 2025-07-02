"""
Problem: Valid Sudoku
LeetCode: https://leetcode.com/problems/valid-sudoku/

Determine if a 9x9 Sudoku board is valid.
Only the filled cells need to be validated according to these rules:
1. Each row must contain the digits 1–9 **without repetition**.
2. Each column must contain the digits 1–9 **without repetition**.
3. Each of the 9 sub-boxes (3x3) must contain the digits 1–9 **without repetition**.

-----------------------------------------------------------
🧠 Approach: HashSets for Rows, Columns, and Squares

- Use 3 hashmaps with sets:
    - `rowSet`: maps each row to a set of digits seen so far.
    - `colSet`: maps each column to a set of digits seen so far.
    - `squares`: maps each 3x3 box to a set of digits. Key is `(r // 3, c // 3)`.

- If a digit already exists in any of the sets for its row, column, or square → return False.
- Otherwise, add it to the respective sets.

-----------------------------------------------------------
Example:

Input:
board = 
[
 ["5","3",".",".","7",".",".",".","."],
 ["6",".",".","1","9","5",".",".","."],
 [".","9","8",".",".",".",".","6","."],
 ["8",".",".",".","6",".",".",".","3"],
 ["4",".",".","8",".","3",".",".","1"],
 ["7",".",".",".","2",".",".",".","6"],
 [".","6",".",".",".",".","2","8","."],
 [".",".",".","4","1","9",".",".","5"],
 [".",".",".",".","8",".",".","7","9"]
]

Check cell [0][0] = "5":
- It's not in rowSet[0], colSet[0], or squares[(0,0)] → Add it.

Check cell [1][0] = "6":
- It's not in rowSet[1], colSet[0], or squares[(0,0)] → Add it.

Check cell [0][1] = "3":
- It's not in rowSet[0], colSet[1], or squares[(0,0)] → Add it.

...and so on

If a duplicate like "5" is found again in row 0 or col 0 or square (0,0), return False.

-----------------------------------------------------------
🕒 Time Complexity: O(1)
- Technically O(9²) = O(81), which is constant for a 9x9 grid.

🧠 Space Complexity: O(1)
- Uses fixed-size maps for 9 rows, 9 columns, and 9 squares.

-----------------------------------------------------------
"""

from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        squares = defaultdict(set)  # Key = (r//3, c//3)

        for r in range(len(board)):
            for c in range(len(board[r])):
                val = board[r][c]

                if val == ".":
                    continue

                # If value already seen in current row, column, or square → invalid
                if (val in rowSet[r] or
                    val in colSet[c] or
                    val in squares[(r // 3, c // 3)]):
                    return False

                # Add value to respective sets
                rowSet[r].add(val)
                colSet[c].add(val)
                squares[(r // 3, c // 3)].add(val)

        return True
