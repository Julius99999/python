# def search_insert(nums, target):
#     left, right = 0, len(nums) - 1
#
#     while left <= right:
#         mid = left + (right - left) // 2
#
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return left
#
# sorted_array = [1, 3, 5, 6]
# target_value = 5
# result = search_insert(sorted_array, target_value)
# print(f"目标值 {target_value} 在排序数组中的索引为 {result}。")
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left
nums=[1,3,5,6]
target=5
result = Solution().searchInsert(nums,target)
print(f"目标值 {target} 在排序数组中的索引为 {result}。")
