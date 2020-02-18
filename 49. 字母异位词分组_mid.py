# 给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

# 示例:
# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"],
# 输出:
# [
  # ["ate","eat","tea"],
  # ["nat","tan"],
  # ["bat"]
# ]
# 说明：所有输入均为小写字母。不考虑答案输出的顺序。

### Solution1:排序单词分类
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        # 新建一个字典用于存储各自输出数列的索引
        word_dict = dict()
        idx = 0
        for w in strs:
            # sorted()返回一个排序列表，列表不能当作字典的键名，在这里将其转换为字符串
            w_s = ''.join(sorted(w))
            # 如果已有此类序列，直接加到result中相应的列表
            if w_s in word_dict:
                result[word_dict[w_s]].append(w)
            # 新的序列加到result的新列表中，同时记录到字典
            else:
                word_dict[w_s] = idx
                idx += 1
                result.append([w])
        return result

### Solution2:排序单词分类plus
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 新建一个字典用于存储各类序列
        word_dict = dict()
        for w in strs:
            # sorted()返回一个排序列表，列表不能当作字典的键名，在这里将其转换为字符串
            w_s = ''.join(sorted(w))
            # 如果已有此类序列，直接加到字典相应key的value中
            if w_s in word_dict:
                word_dict[w_s].append(w)
            # 作为新的键值对加到字典中
            else:
                word_dict[w_s] = [w]
        # dict.values()返回字典中所有的值到迭代器中，可用list()转为列表（不转也能通过，亲测）
        return list(word_dict.values())

### Solution3:字母计数分类，用26个数字组成的列表表示26个字母的计数，转为元组后写入字典
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 新建一个字典用于存储各类序列
        word_dict = dict()
        for word in strs:
            # 字典的键用26个数字的列表表示
            count = [0]*26
            for w in word:
                # ord()函数可得到ascll值，w减'a'得到ascll值之差即为列表索引，加1
                count[ord(w)-ord('a')] += 1
            # 列表转为元组（注意：字典的键不能是列表，元组中的值不能改变），将word加到字典的对应位置的value中
            count = tuple(count)
            if count in word_dict:
                word_dict[count].append(word)
            else:
                word_dict[count] = [word]
        # dict.values()返回字典中所有的值到迭代器中，可用list()转为列表（不转也能通过，亲测）
        return list(word_dict.values())

### Solution4:正整数的唯一分解定理
### 每个大于1的自然数，要么本身就是质数，要么可以写为2个以上的质数的积，而且这些质因子按大小排列之后，写法仅有一种方式
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 建立一个列表来表示26个质数
        prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
        # 建立字典
        word_dict = dict()
        for word in strs:
            product = 1
            for w in word:
                product *= prime[ord(w)-ord('a')]
            if product in word_dict:
                word_dict[product].append(word)
            else:
                word_dict[product] = [word]
        return list(word_dict.values())
