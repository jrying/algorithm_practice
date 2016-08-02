import heapq

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        arr = []
        for i in range(min(len(nums1), k)):
            for j in range(min(len(nums2), k)):
                arr.append((nums1[i] + nums2[j], nums1[i], nums2[j]))
        heapq.heapify(arr)
        return map(lambda x: [x[1], x[2]], heapq.nsmallest(k, arr))
