# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

# 示例:
# board =
# [
  # ['A','B','C','E'],
  # ['S','F','C','S'],
  # ['A','D','E','E']
# ]
# 给定 word = "ABCCED", 返回 true
# 给定 word = "SEE", 返回 true
# 给定 word = "ABCB", 返回 false


###Solution: 回溯法:从每个点开始进行深度搜索，建立一个标记矩阵同步遍历过程，对匹配点标记为1
### 当字符匹配时继续深度搜索，失败时回溯到上一个字符向另一个广度进行搜索
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        height, width = len(board), len(board[0])
        # 初始化二维数组要用for_range不能用*形式，因为*形式后面赋值一个点会赋一列导致出错
        flag = [[0 for _ in range(width)] for _ in range(height)]

        def search(deep, h, w):
            if not (0<=h<height and 0<=w<width):
                return False
            # 当前字符匹配且flag为0
            if word[deep]==board[h][w] and flag[h][w]==0:
                flag[h][w] = 1
                # 如果word已经全部匹配完毕，返回True
                if deep==len(word)-1:
                    return True
                # 否则，向临近点按上下左右顺序进行下一个字符的匹配
                # 如果临近点均不匹配，则此处flag变回0，回溯到上一个点
                else:
                    # 上
                    if search(deep+1, h-1, w):
                        return True
                    # 下
                    elif search(deep+1, h+1, w):
                        return True
                    # 左
                    elif search(deep+1, h, w-1):
                        return True
                    # 右
                    elif search(deep+1, h, w+1):
                        return True
                    else:
                        flag[h][w] = 0
                        return False
            # 当前字符不匹配，返回False
            else:
                return False


        for h in range(height):
            for w in range(width):
                # 从(h,w)位置进入搜索第1个字符word[0]
                if search(0, h, w):
                    return True
        return False
