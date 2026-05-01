class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hash_set = {i:[0] * 9 for i in range(0, 27)}

        for i in range(0, 9):
            for j in range(0, 9):
                curr_num = board[i][j]
                if board[i][j] == ".":
                    continue
                else:
                    curr_num = int(curr_num) - 1
                
                if hash_set[i][curr_num] != 1:
                    hash_set[i][curr_num] = 1
                else:
                    return False

                if hash_set[j + 9][curr_num] != 1:
                    hash_set[j + 9][curr_num] = 1
                else:
                    return False

                curr_quad = self.checkQuadrant(i, j) + 18
                if hash_set[curr_quad][curr_num] != 1:
                    hash_set[curr_quad][curr_num] = 1
                else:
                    return False

        return True

    def checkQuadrant(self, i, j) -> int:
        if i < 3:
            if j < 3:
                return 0
            elif j < 6:
                return 1
            elif j < 9:
                return 2
        elif i < 6:
            if j < 3:
                return 3
            elif j < 6:
                return 4
            elif j < 9:
                return 5
        else:
            if j < 3:
                return 6
            elif j < 6:
                return 7
            else:
                return 8