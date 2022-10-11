class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        # base case
        if (len(nums) == 1):
            return [nums.copy()]
        
        # next we will go every value in nums
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)
            
            for perm in perms:
                perm.append(n)
            result.extend(perms) # in python, if we want to add multiple values in a list/array, just use extend
            nums.append(n)
        
        return result
