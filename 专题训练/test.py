
#冒泡要记得标志位，最好O(n),平均、最坏，稳定
#插入要记得是交换，或者不交换最后插入即可.最好O(n),平均、最坏。稳定。插入比冒泡好在没有那么多的交换
#快排回顾partition过程。最好O(nlogn),平均最坏O(n2)，不稳定
#归并记得切割left、right的函数要有基线。全部都是O(nlogn)，稳定

class Solution:
    def bubble(self,l):
        n = len(l)
        for i in range(n-1,0,-1):
            flag = 1
            for j in range(i):
                if l[j] > l[j+1]:
                    flag = 0
                    l[j],l[j+1] = l[j+1],l[j]
            if flag:return l
        return l

    def insert(self,l):
        n = len(l)
        for i in range(1,n):
            for j in range(i,-1,-1):
                if l[j] < l[j-1]:
                    l[j],l[j-1] = l[j-1],l[j]
                else:
                    break
        return l


    def quick_sort(self,l):
        left = 0
        right = len(l) -1
        self.q_sort(left,right,l)
        return l

    def q_sort(self,left,right,l):
        if left < right:
            pivot = self.partition(l,left,right)
            self.q_sort(left,pivot-1,l)
            self.q_sort(pivot+1,right,l)

    def partition(self,l,left,right) -> int:
        pivot = l[left]
        while left < right:
            while left < right and l[right] >= pivot:
                right -= 1
            l[left] = l[right]
            while left < right and l[left] < pivot:
                left += 1
            l[right] = l[left]
        l[left] = pivot
        return left

    def q_merge(self,l):
        if len(l) == 1:return l
        mid = (0+len(l)) >> 1
        left = self.q_merge(l[:mid])
        right = self.q_merge(l[mid:])
        return self.merge(left,right)

    def merge(self,left,right):
        i = j = 0
        res = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res += left[i:] or right[j:]
        return res


l1 = [6,5,4,3,2,1,1,8,8,9,2,5,1,7,6,4,3,1,8,8,9,2,5]
l2 = [6,5,4,3,2,1,1,8,8,9,2,5,1,7,6,4,3,1,8,8,9,2,5]
l3 = [6,5,4,3,2,1,1,8,8,9,2,5,1,7,6,4,3,1,8,8,9,2,5]
l4 = [6,5,4,3,2,1,1,8,8,9,2,5,1,7,6,4,3,1,8,8,9,2,5]
a = Solution()
print(a.bubble(l1))
print(a.insert(l2))
print(a.quick_sort(l3))
print(a.q_merge(l4))


class Solution2:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

    def preorder(self,root):
        res = []
        self.pre_helper(root,res)
        return res

    def pre_helper(self,root,res):
        if root:
            res.append(root.val)
            self.pre_helper(root.left,res)
            self.pre_helper(root.right,res)

    def inorder(self,root):
        res = []
        self.in_helper(root,res)
        return res

    def in_helper(self,root,res):
        if root:
            self.in_helper(root.left,res)
            res.append(root.val)
            self.in_helper(root.right, res)

    def pre_order(self,root):
        res,stack = [],[]
        stack.append(root)
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res

    def in_order(self,root):
        res,stack = [],[]
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right


class LinkNode:
    def __init__(self):
        self.next = None

class Solution3:
    def reverselist(self,head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return curr

    def middlelink(self,head):
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

    def cyclelink(self,head):
        fast = slow = head
        while fast==slow:
            fast = fast.next.next
            slow = slow.next
        while head != slow:
            head = head.next
        return head

    def mergelink(self,l1,l2):
        prev = curr = LinkNode()
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return prev.next

    def deletenode(self,head,val):
        if head.val == val:
            return head.next
        curr = head
        while head and head.next:
            if head.next.val == val:
                head.next = head.next.next
        return curr

    def deletelastn(self,n,head):
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next =slow.next.next
        return head


class Solution4:
    def combination_sum(self,candidates,target):
        self.res = []
        self.dfs(0,candidates,target,[])
        return self.res

    def dfs(self,index,candidates,target,path):
        if target <0:return
        if target == 0:
            self.res.append(path)
            return
        for i in range(index,len(candidates)):
            self.dfs(i,candidates,target-candidates[i],path+candidates[i])






