class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()  # Trie les éléments pour que les doublons soient côte à côte
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False