# https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums):

        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            print("prefix: ", prefix)
            print("res: ", res)

            res[i] = prefix
            prefix *= nums[i]
        print("finaly, prefix and res are: ", prefix, res)
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            print("postfix: ", postfix)
            print("res: ", res)
            res[i] *= postfix
            postfix *= nums[i]
        print("finaly, postfix and res are: ", postfix, res)
        return res
sol = Solution()

nums = [1,2,3,4]

result = sol.productExceptSelf(nums)

print(result)