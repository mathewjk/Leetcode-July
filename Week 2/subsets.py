class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def helper(index=0, curr=[]):
            if index >= len(nums):
                result.append(curr.copy())
                return

            curr.append(nums[index])
            helper(index + 1, curr)
            curr.pop()
            helper(index + 1, curr)

        helper()

        return result
