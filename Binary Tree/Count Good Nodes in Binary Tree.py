# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, maxVal):
            if not node:
                return 0
            
            # if particular noder is good or not, let's compute that in our result if 
            res = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            
            #since this dfs function is just counting the numbers of good nodes, we can just the result of the function and add it to our result
            res += dfs(node.left, maxVal) 
            res += dfs(node.right, maxVal)
            return res
        
        # we want compute for the entire tree, so when we call our dfs, we call it on the root node
        return dfs(root, root.val) # for the root node, we are just passing its own value as maxVal
        
        '''My initial thought
           else:
                maxVal = 0
                count = 0
                if node.val > maxVal:
                    count += 1
                    maxVal = max(maxVal, node.val)
                    dfs(node.left, maxVal)
                    dfs(node.right, maxVal)
                else:
                    maxVal = maxVal
                    dfs(node.left, maxVal)
                    dfs(node.right, maxVal)
            
                
        return count'''     
                
        
