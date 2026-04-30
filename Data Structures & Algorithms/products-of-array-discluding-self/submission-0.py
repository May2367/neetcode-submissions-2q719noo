class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Brute Force / Naive Solution
        output = [1] * len(nums)
        
        for i in range(0, len(nums)):
            #iterate over the remaining elements and multiply them together
            for j in range(0, len(nums)):
                if j != i:
                    output[i] *= nums[j]

        return output