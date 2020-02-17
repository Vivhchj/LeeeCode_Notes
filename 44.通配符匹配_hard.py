### Solution1:回溯法
### 同时遍历，依次匹配s和p中的各元素，如果相对应的字符相同或遇到'?'，则直接匹配，双双后移；若未遇到'*'时就匹配失败，则False
### 要详细讨论的是'*'的情况：
### 1 每次遇到'*'，记住星号的位置p_star，以及相对应开始检索的位置s_star，从s_star开始与p_star+1开始匹配
###    1.1 若匹配失败，将s_star+=1，从s_star(更新后)和p_star+1处开始重新匹配（可能是因为过早结束'*'的匹配，如'abcbac'与'a*bac'会在第一个b就进入'*'后的检测，导致'c'匹配失败）
###    1.2 若匹配成功，继续后面的匹配
###    1.3 若p匹配结束而s有剩余则继续1.1的操作
### 2 最后若s匹配结束而p有剩余，且剩余部分为'*'则为True，否则为False
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        idx_s = 0
        s_len, p_len = len(s), len(p)
        if s_len>0 and p_len==0:
            return False
        if s_len==0 and p_len>0:
            for pi in p:
                if pi != '*':
                    return False
            return True
        s_idx, p_idx = 0, 0
        s_star, p_star = -1, -1
        while s_idx < s_len:
            # 两两匹配时，双双后移继续匹配下一对
            if p[p_idx]=='?' or p[p_idx]==s[s_idx]:
                s_idx += 1
                p_idx += 1
                # 如果p匹配完而s有剩余，先看p有没有'*'，有的话更新s_star+=1，从s_star和p_star+1重新开始匹配'*'后字符串；否则False
                if p_idx > p_len - 1 and s_idx < s_len:
                    if p_star != -1:
                        s_star += 1
                        s_idx = s_star
                        p_idx = p_star + 1
                    else:
                        return False
            # 如果遇到'*'
            elif p[p_idx]=='*':
                # 如果'*'不是末尾，记住p_star与s_star作为回溯点，进行后续匹配
                if p_idx < p_len-1:
                    p_star = p_idx
                    p_idx += 1
                    s_star = s_idx
                # 如果'*'是末尾，则True
                else:
                    return True
            # 不匹配时，如果没有'*'出现过，直接False；否则回溯重新匹配
            else:
                if p_star != -1:
                    s_star += 1
                    s_idx = s_star
                    p_idx = p_star + 1
                else:
                    return False
        # 如果s匹配结束而p有剩余，判断是否剩下的全是'*'，是的话True，不是的话False
        if p_idx < p_len:
            while p_idx < p_len:
                if p[p_idx] != '*':
                    return False
                p_idx += 1
            return True
        else:
            return True

### Solution2:回溯法_plus
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        idx_s = 0
        s_len, p_len = len(s), len(p)
        if s_len>0 and p_len==0:
            return False
        if s_len==0 and p_len>0:
            for pi in p:
                if pi != '*':
                    return False
            return True
        s_idx, p_idx = 0, 0
        s_star, p_star = -1, -1
        while s_idx < s_len:
            # 两两匹配时，双双后移继续匹配下一对
            ### 这里添加一个判断p是否匹配完
            if p_idx < p_len and (p[p_idx]=='?' or p[p_idx]==s[s_idx]):
                s_idx += 1
                p_idx += 1
                ### 这里判断p匹配完而s有剩余有些超前，即使这里不判断，转到下一个循环同样可以判断出来
                # # 如果p匹配完而s有剩余，先看p有没有'*'，有的话更新s_star+=1，从s_star和p_star+1重新开始匹配'*'后字符串；否则False
                # if p_idx > p_len - 1 and s_idx < s_len:
                #     if p_star != -1:
                #         s_star += 1
                #         s_idx = s_star
                #         p_idx = p_star + 1
                #     else:
                #         return False
            # 如果遇到'*'
            ### 同样添加一个p是否匹配完的判断
            elif p_idx < p_len and p[p_idx]=='*':
                p_star = p_idx
                p_idx += 1
                s_star = s_idx
                ### 不需要判断'*'是否是末尾，只需要当p达到末尾时，判断如果前面有过'*'，就回溯匹配即可
                # # 如果'*'不是末尾，记住p_star与s_star作为回溯点，进行后续匹配
                # if p_idx < p_len-1:
                #     p_star = p_idx
                #     p_idx += 1
                #     s_star = s_idx
                # # 如果'*'是末尾，则True
                # else:
                #     return True
            ### 这里可以将"else: if ... else ..."合并为"elif ... else ..."
            elif p_star != -1:
                s_star += 1
                s_idx = s_star
                p_idx = p_star + 1
            else:
                return False
            # # 不匹配时或p匹配完时，如果前面有'*'出现过，回溯重新匹配；否则直接False
            # else:
            #     if p_star != -1:
            #         s_star += 1
            #         s_idx = s_star
            #         p_idx = p_star + 1
            #     else:
            #         return False
        ### s遍历完来到这里会有两种情况，一种是p没有剩余为True，一种是p有剩余，有剩余时如果全剩'*'，为True，否则False
        ### 可以用p_idx进行巧妙判断
        while p_idx < p_len:
            if p[p_idx]=='*':
                p_idx += 1
            else:
                break
        ## 秒啊！！！
        return p_idx == p_len

        # # 如果s匹配结束而p有剩余，判断是否剩下的全是'*'，是的话True，不是的话False
        # if p_idx < p_len:
        #     while p_idx < p_len:
        #         if p[p_idx] != '*':
        #             return False
        #         p_idx += 1
        #     return True
        # else:
        #     return True

