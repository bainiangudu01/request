class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


def LinkList(l):
    head = Node(l[0])
    tail = head
    for i in l[1:]:
        tail.next = Node(i)
        tail = Node(i)
    return head, tail


while True:
    try:
        n = int(input())
        l = input().split()
        k = int(input())
        head, tail = LinkList(l)


        def bianli(lk):
            while lk:
                print(lk.item)
                lk = lk.next
                if lk==

    except:
        break


class Node(object):
    def __init__(self, val=0):
        self.val = val
        self.next = None


while True:
    try:
        head = Node()
        count, num_list, k = int(input()), list(map(int, input().split())), int(input())
        while k:
            head.next = Node(num_list.pop())
            head = head.next
            k -= 1
        print(head.val)
    except EOFError:
        break
