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

                curr_quad = (i//3) * 3 + (j//3) + 18
                if hash_set[curr_quad][curr_num] != 1:
                    hash_set[curr_quad][curr_num] = 1
                else:
                    return False

        return True