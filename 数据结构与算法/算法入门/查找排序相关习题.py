# 排序的思路
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = list(s)  # 因为字符串在python中是不可变的元素，不能排序，所以先将字符串转换为列表
        tt = list(t)
        ss.sort()
        tt.sort()
        return ss == tt  # 如果ss等于tt，返回true；如果不等于返回false


# 或者一行写完
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(list(s)) == sorted(list(t))


# 字典的角度，统计字符及出现的次数
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}
        for i in s:
            dict1[i] = dict1.get(i, 0) + 1  # 将i出现的次数加1，如果开始没有i键，设置0
        for i in t:
            dict2[i] = dict2.get(i, 0) + 1
        return dict1 == dict2


# 普通写法
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for line in matrix:
            if target in line:
                return True
        return False


# 二分查找写法
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        l = len(matrix[0])  # matrix列表的长和每行小列表的长一致，就是matrix列表中索引为0的小列表的长度
        if l == 0:  # 避免长是0，即大列表中第一个小列表是空列表
            return False
        w = len(matrix)  # w是宽，一个小列表占一行，matrix中有几个小列表宽就是多少
        if w == 0:  # 避免宽是0，即大列表中只有一行小列表，不然right会变负值
            return False
        left = 0
        right = l * w - 1
        while left <= right:
            mid = (left + right) // 2
            i = mid // l  # 将mid的值转换为(i,j)形式
            j = mid % l
            if matrix[i][j] == target:  # matrix[i][j]对应的是mid位置的数
                return True
            elif matrix[i][j] > target:
                right = mid - 1
            else:
                left = mid + 1
        else:
            return False


# 普通做法
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):  # 遍历nums列表中i之后的元素，也可以遍历之前的元素
                if nums[i] + nums[j] == target:
                    return i, j


# 二分查找做法
class Solution:
    def binary_serch(self, l, a, left, right):  # 将二分查找的left和right作为参数
        while left <= right:
            mid = (left + right) // 2
            if l[mid][0] == a:
                return mid
            elif l[mid][0] > a:
                right = mid - 1
            else:
                left = mid + 1
        else:
            return None  # 如果循环完没有找到，返回None

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        new_nums = [[num, i] for i, num in enumerate(nums)]  # 新建一个二维列表，每一行有两个数字，第一个是数字，第二个是下标
        new_nums.sort(key=lambda x: x[0])  # 二维列表按照key进行排序，x[0]是列表的第一个下标元素，即num

        for i in range(len(new_nums)):
            a = new_nums[i][0]
            b = target - a
            if b >= a:
                j = self.binary_serch(new_nums, b, i + 1, len(nums) - 1)
            else:
                j = self.binary_serch(new_nums, b, 0, i - 1)
            if j:
                break  # 如果找到j，跳出
        return sorted([new_nums[i][1], new_nums[j][1]])
