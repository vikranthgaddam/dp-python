from typing import List
class Solution:
    def houseRobber(self,nums:List[int],n:int)->int:
        length=len(nums)
        
        if (length<0):
            return 0
        if length==0:
            return nums[0]
        pick =nums[length]
        return 
    def recursiveSum(nums:List[int],n:int)->int:
        if n==0:
            return nums[0]
        if n<0:
            return 0
        pick=nums[n]+recursiveSum(nums,n-2)
        notPicked=recursiveSum(nums,n-1)
        return max(pick,notPicked)