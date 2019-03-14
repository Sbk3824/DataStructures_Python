
class solution(object):
    def twoSum(self, nums, target):
    
        lookup = {}
    
        for i, num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target-num],i)
            lookup[num] = i
        
print solution().twoSum((2,7,11,15),18)
