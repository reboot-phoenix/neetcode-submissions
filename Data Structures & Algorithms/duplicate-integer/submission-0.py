class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        has_dublicates = len(nums) != len(set(nums))
        if (has_dublicates == True):
            return True
        else:
            return False
