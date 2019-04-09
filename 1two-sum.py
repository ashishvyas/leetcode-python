class Solution(object):
  def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """

    indexMap = {}
    for i in xrange(len(nums)):
      if nums[i] in indexMap:
        return [indexMap[nums[i]], i]
      else:
        indexMap[target-nums[i]] = i

	
        
if __name__ == "__main__":
  sol = Solution()
  print sol.twoSum([2,5,7,9,11], 12)
