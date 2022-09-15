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
      
      
