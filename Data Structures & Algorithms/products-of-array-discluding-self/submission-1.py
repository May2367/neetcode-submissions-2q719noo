class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)

        output = [1] * length
        prefix = [1] * length
        suffix = [1] * length

        prefix[0] = 1
        suffix[length - 1] = 1

        for i in range(1, length):
            prefix[i] *= prefix[i - 1] * nums[i - 1]
            suffix[length - i - 1] *= suffix[length - i] * nums[length - i]

        for i in range(0, length):
            output[i] = prefix[i] * suffix[i]

        return output