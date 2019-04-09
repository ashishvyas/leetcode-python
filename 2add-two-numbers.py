# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution(object):
  def addTwoNumbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    ans = l = ListNode(0)
    carry = 0
    while l1 or l2 or carry: 
      v1 = v2 = 0
      if l1:
        v1 = l1.val
        l1 = l1.next
      
      if l2:
        v2 = l2.val
        l2 = l2.next
        
      v = (v1 + v2 + carry)
      if (v >= 10):
        carry = 1
        v = v - 10
      else: 
        carry = 0
      l.next = ListNode(v)
      l = l.next
      print "Added node to list with value ", v, carry
    return ans.next
       

if __name__ == '__main__':
  sol = Solution()

  l1 = ListNode(2)
  l1.next = ListNode(4)
  l1.next.next = ListNode(3)
  l2 = ListNode(5)
  l2.next = ListNode(6)
  l2.next.next = ListNode(4)
  res = sol.addTwoNumbers(l1, l2)
  while res:
    print res.val
    res = res.next


  l1 = ListNode(0)
  l2 = ListNode(5)
  l2.next = ListNode(6)
  l2.next.next = ListNode(4)
  res = sol.addTwoNumbers(l1, l2)
  while res:
    print res.val
    res = res.next


  l1 = ListNode(0)
  l1.next = ListNode(9)
  l1.next.next = ListNode(3)
  l2 = ListNode(1)
  l2.next = ListNode(1)
  res = sol.addTwoNumbers(l1, l2)
  while res:
    print res.val
    res = res.next
