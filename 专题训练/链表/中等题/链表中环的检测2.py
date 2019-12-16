


class Solution:
    def cycleList2(self,head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None

        while head != slow:
            slow,head = slow.next,head.next
        return head

    def cycleList22(self,head):
        visited = set()
        while head:
            if head in visited:
                return head
            visited.add(head)
            head = head.next
        return None