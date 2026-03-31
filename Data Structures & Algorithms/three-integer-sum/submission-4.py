class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        nums.sort()
        for i in range(n-2):
            value = -nums[i]
            l, r = i+1, n-1
            while l < r:
                if nums[l]+nums[r]== value:
                    if [nums[i],nums[l],nums[r]] not in result:
                        result.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                elif nums[l]+nums[r]<value:
                    l+=1
                else:
                    r-=1
        return result
