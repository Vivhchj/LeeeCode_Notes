# 判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。
# 数字 1-9 在每一行只能出现一次。
# 数字 1-9 在每一列只能出现一次。
# 数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。
# 数独部分空格内已填入了数字，空白格用 '.' 表示。

# 示例 1:
# 输入:
# [
  # ["5","3",".",".","7",".",".",".","."],
  # ["6",".",".","1","9","5",".",".","."],
  # [".","9","8",".",".",".",".","6","."],
  # ["8",".",".",".","6",".",".",".","3"],
  # ["4",".",".","8",".","3",".",".","1"],
  # ["7",".",".",".","2",".",".",".","6"],
  # [".","6",".",".",".",".","2","8","."],
  # [".",".",".","4","1","9",".",".","5"],
  # [".",".",".",".","8",".",".","7","9"]
# ]
# 输出: true

# 示例 2:
# 输入:
# [
#   ["8","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# 输出: false
# 解释: 除了第一行的第一个数字从 5 改为 8 以外，空格内其他数字均与 示例1 相同。
     # 但由于位于左上角的 3x3 宫内有两个 8 存在, 因此这个数独是无效的。
# 说明:
# 一个有效的数独（部分已被填充）不一定是可解的。
# 只需要根据以上规则，验证已经填入的数字是否有效即可。
# 给定数独序列只包含数字 1-9 和字符 '.' 。
# 给定数独永远是 9x9 形式的。

### Solution1: List判断重复法，将每次要判断的9个位置的数字逐次加入一个新List中，若已有此数字则表示无效
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 9x9固定范围，根据三个条件用一次遍历进行判定，只要出现了一个不符合条件的情况就输出False
        result = True
        width, height = 9, 9
        arr_h, arr_w, arr_q = [], [], []
        # 一次遍历，全部检测
        for i in range(9):
            for j in range(9):
                # 检测单行
                if board[i][j] != '.':
                    if board[i][j] in arr_w:
                        result = False
                        break
                    else:
                        arr_w.append(board[i][j])
                # 检测单列
                if board[j][i] != '.':
                    if board[j][i] in arr_h:
                        result = False
                        break
                    else:
                        arr_h.append(board[j][i])
                # 检测3x3方格
                if i%3==0 and j%3==0:
                    for k in range(3):
                        for l in range(3):
                            if board[i+k][j+l] != '.':
                                if board[i+k][j+l] in arr_q:
                                    result = False
                                    break
                                else:
                                    arr_q.append(board[i+k][j+l])
                        if result == False:
                            break
                if result == False:
                    break        
                arr_q.clear()
            arr_w.clear()
            arr_h.clear()
            if result == False:
                break
        return result

### Solution2:位图法，用一个9位的二进制表示9个数字的有1无0
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 9x9固定范围，根据三个条件用一次遍历进行判定，只要出现了一个不符合条件的情况就输出False
        # 位图法，用9位二进制表示一条
        result = True
        arr_w, arr_h, arr_q = 0, 0, 0 
        for i in range(9):
            arr_w = arr_w >> 9
            arr_h = arr_h >> 9
            for j in range(9):
                # 每一横行
                if board[i][j] != '.':
                    # 关键步
                    # 计算需要移位的步数
                    step = int(board[i][j])-1
                    # 判断该位置是否为0
                    if (arr_w >> step) & 1 == 0:
                        # 是的话将该位置改为1
                        arr_w = arr_w | (1 << step)
                    else:
                        # 否则该九宫格无效
                        result = False
                else:
                    pass
                # 每一竖列
                if board[j][i] != '.':
                    step = int(board[j][i])-1
                    if (arr_h >> step) & 1 == 0:
                        arr_h = arr_h | (1 << step)
                    else:
                        result = False
                else:
                    pass
                # 9个3x3方格
                if i%3==0 and j%3==0:
                    arr_q = arr_q >> 9
                    for k in range(3):
                        for l in range(3):
                            if board[i+k][j+l] != '.':
                                step = int(board[i+k][j+l])-1
                                if (arr_q >> step) & 1 == 0:
                                    arr_q = arr_q | (1 << step)
                                else:
                                    result = False
                                    break
                            else:
                                pass
                        if result == False:
                            break
                if result == False:
                    break
        return result
                    

                    

