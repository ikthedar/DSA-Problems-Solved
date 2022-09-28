class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool: # s1=abc, s2 = baxyzbca
        h1 = Counter(s1) # a = 1, b = 1, c = 1
        n = len(s1) # 3
        
        for i in range(len(s2) - len(s1) + 1): # range(8 - 3 + 1) = range(4) because no need to move if 2 characters left
            h2 = Counter(s2[i : i + n]) # for example, if i x, we will use Counter from x to z: x = 1, y = 1, z = 1
            
            if h1 == h2:
                return True
        
        return False
            
        
        
        '''# if length of s1 is greater than s2, no need to further check anything
        if len(s1) > len(s2):
            return False
        
        # initializing two dictionaries for each string
        count1 = {}
        count2 = {}
        
        # iterating through the first string and adding each char in the dict; this dict will remain same
        for i in range(len(s1)):
            count1[s1[i]] = 1 + count1.get(s1[i], 0)
            
        # initializing a Sliding Window to iterate thru the second string    
        l = 0
        for r in range(len(s2)):
            # in the 2nd dict, we will add char only if it is in 1st dict and not already in 2nd dict
            
            if s2[r] in count1 and s2[r] not in count2:
                count2[s2[r]] = 1 + count2.get(s2[r], 0)
            
            if (r - l + 1) < len(s1):
                r += 1
                
            elif (r - l + 1) > len(s1):
                # before shifting the l pointer, removing its char from dict
                if s2[l] in count2:
                    count2.pop(s2[l])
                l += 1
                if count1.keys() == count2.keys():
                    return True
                else:
                    r += 1
                    
            else:
                if count1.keys() == count2.keys():
                    return True
                else:
                    r += 1
        return False'''
