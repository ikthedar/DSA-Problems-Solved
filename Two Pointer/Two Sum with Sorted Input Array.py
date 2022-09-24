class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        curSum = 0
        
        # We need a loop to iterate through our array
        # The condition here is left is greater than right, though it doesn't really matter in this case since we are guaranteed to have a solution/ target
        while l < r:
            curSum = numbers[l] + numbers[r]
            
            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l+1, r+1] #since the the array is 1-indexed as given in the question
        
        return []
