class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Brute Force / Naive Solution
        length = len(nums)
        output = [1] * length
        
        for i in range(0, length):
            for j in range(0, length):
                if j != i:
                    output[i] *= nums[j]

        return output

        #Run Time: O(n^2)
        #Space Complexity: O(n)

        #How could we optimize this?
        #Possibly loop through the array only once, then for each value 
        #in the array, multiply it against all indices of output except 
        #for it's own