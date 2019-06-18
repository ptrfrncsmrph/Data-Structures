"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""

    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""

    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """
    For debugging
    """

    def __repr__(self):
        node = self.head
        string = ""
        if node is None:
            return "[ ]"
        while node.next is not None:
            string += f"{node.value}, "
            node = node.next
        return f"[ {string}{node.value} ]"

    def add_to_head(self, value):
        if self.length == 0:
            node = ListNode(value)
            self.head = node
            self.tail = node
        else:
            self.head.insert_before(value)
            self.head = self.head.prev
        self.length += 1

    def remove_from_head(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            node = self.head
            self.tail = None
            self.head = None
            self.length -= 1
            return node.value
        else:
            node = self.head
            self.head.delete()
            self.head = self.head.next
            self.length -= 1
            return node.value

    def add_to_tail(self, value):
        if self.length == 0:
            node = ListNode(value)
            self.tail = node
            self.head = node
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next
        self.length += 1

    def remove_from_tail(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            node = self.tail
            self.head = None
            self.tail = None
            self.length -= 1
            return node.value
        else:
            node = self.tail
            self.tail = self.tail.prev
            self.length -= 1
            return node.value

    def move_to_front(self, node):
        if node == self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node.delete()
        node.prev, node.next = None, self.head
        self.head.prev = node
        self.head = node

    def move_to_end(self, node):
        if node == self.head:
            self.head = self.head.next
            self.head.prev = None
        else:
            node.delete()
        node.prev, node.next = self.tail, None
        self.tail.next = node
        self.tail = node

    def delete(self, node):
        if node == self.head:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
        if node == self.tail:
            self.tail = self.tail.prev
            if self.tail is not None:
                self.tail.next = None
        else:
            node.delete()
        self.length -= 1

    def get_max(self):
        if self.length == 0:
            return None
        max = self.head.value
        node = self.head.next
        while node is not None:
            if node.value > max:
                max = node.value
            node = node.next
        return max
