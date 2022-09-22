'''
78. Subsets

APPROACH 1: Array manipulation approach
TIME COMPLEXITY: O(2 ** N))
SPACE COMPLEXITY: O(1)
LEETCODE: Yes
DIFFICULTIES: nope, solved after the class

APPROACH 2: Backtracking 01 method
TIME COMPLEXITY: O(2 ** N)
SPACE COMPLEXITY: O(N)
LEETCODE: Yes
DIFFICULTIES: Nope, solved after the class

'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # Array Manipulation
        def approach1(nums):
            res = []
            res.append([])
            
            for i in range(0,len(nums)):
                sz = len(res)
                for j in range(0, sz):
                    # print((res[j]))
                    temp = res[j].copy()
                    temp.append(nums[i])
                    res.append(temp)
            return res
        
        
        def approach2(nums):
            global whole, res
            whole = nums
            res = []
            
            def rec(idx, path):
                global whole, res
                # base
                if idx == len(whole):
                    res.append(path.copy())
                    return
                
                # logic
                # not choose
                rec(idx+1, path)
                
                # choose
                # insert
                path.append(whole[idx])
                # recurse
                rec(idx+1, path)
                # backtrack
                path.pop()
                
            rec(0, [])
            
            return res
        
               
        # return approach1(nums)
        return approach2(nums)
        
