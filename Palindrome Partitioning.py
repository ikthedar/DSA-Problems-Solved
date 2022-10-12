class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = [] # for all the palindrome substrings
        part = [] # for the current substring 
        
        # Entire depth first search backtracking recursive function
        def dfs(i):
            # base case
            if i >= len(s):
                res.append(part.copy())
                return
            # loop for generating every substring from i to j, to check if a palindrom, if not, skip to next iteration of the loop
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        # calling the function, start index is 0
        dfs(0)
        return res
    
    # helper function 
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
