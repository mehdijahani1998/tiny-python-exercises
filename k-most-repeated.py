# https://leetcode.com/problems/top-k-frequent-elements/

from collections import defaultdict


class Solution:
    def topKFrequent(self, nums, k: int):
        def def_value():
            return 0

        repDict = defaultdict(def_value)

        for element in nums:
            repDict[element] += 1

        print("repDict filled: ", repDict)

        numRepSorted = sorted(repDict.items(), key = lambda x : x[1], reverse=True)
        print("numRepSorted is sorted",numRepSorted)

        final_list = []
        for i in range(k):
            final_list.append(numRepSorted[i][0])
        
        print("final_list: ", final_list)

        return final_list

sol = Solution()

nums = [1,1,1,2,2,3]
k = 2

final_sol = sol.topKFrequent(nums, k)

print(final_sol)


