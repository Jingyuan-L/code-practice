class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


n = int(input().strip())
nums1 = list(map(int, input().strip().split()))
m = int(input().strip())
nums2 = list(map(int, input().strip().split()))

l1_dummy = ListNode()
l1 = ListNode(nums1[0])
l1_dummy.next = l1
l2_dummy = ListNode()
l2 = ListNode(nums2[0])
l2_dummy.next = l2
for k in range(1, n):
    node = ListNode(nums1[k])
    l1.next = node
    # print(l1.val)
    l1 = l1.next

for k in range(1, m):
    node = ListNode(nums2[k])
    l2.next = node
    # print(l2.val)
    l2 = l2.next

l1, l2 = l1_dummy.next, l2_dummy.next
res = []
while l1 and l2:
    # print(l1.val, l2.val)
    if l1.val == l2.val:
        res.append(l1.val)
        l1 = l1.next
        l2 = l2.next
    elif l1.val < l2.val:
        l2 = l2.next
    else:
        l1 = l1.next
string = ""
for i in range(len(res)):
    string += str(res[i]) + " "
print(string)