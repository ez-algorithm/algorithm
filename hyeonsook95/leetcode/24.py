class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        answer = head.next
        head = ListNode(0, head)
        try:
            while head.next.next:
                temp = head.next
                head.next = head.next.next
                temp.next = head.next.next
                head.next.next = temp

                head = head.next.next
            return answer
        except:
            head = head.next
            return answer