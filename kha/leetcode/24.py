# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head != None and head.next != None:
            
            next_node = head.next
            #재귀로 가장 끝까지 가서 뒤에서부터 자리를 교환함
            head.next = self.swapPairs(next_node.next)
            #자리를 교환
            next_node.next = head
            
            return next_node
        
        #가장 끝 노드라면 교환없이 바로 반환
        return head
            