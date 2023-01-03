class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        ans = []
        
        vacans = []
        
        if len(changed)%2:
            return ans
        
        changed.sort()
        
        tmp = Counter(changed)
        for i in changed:
            if tmp[i]==0:
                continue
            else:
                if tmp.get(2*i,0) >=1:
                    ans.append(i)
                    tmp[2*i] -= 1
                    tmp[i] -=1
                else:
                    return vacans
        return ans
      
      
# Learned about Counter. https://realpython.com/python-counter/#:~:text=Counter%20is%20a%20subclass%20of,argument%20to%20the%20class's%20constructor.
# Actual question link: https://leetcode.com/problems/find-original-array-from-doubled-array/
