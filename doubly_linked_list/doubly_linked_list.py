"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def __str__(self):
        s = ""
        curr_node = self.head
        while curr_node:
            s += f"{curr_node.value}"
            curr_node = curr_node.next
            s += None

    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """

    def add_to_head(self, value):
        new_node = ListNode(value, None)
        if self.head is None:
            new_node.prev = None
            self.head = self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None
            self.length += 1

    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """

    def remove_from_head(self):
        old_head = self.head
        old_head.next = None
        if self.head == self.tail:
            curr_head = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return curr_head.value

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """

    def add_to_tail(self, value, new_node=None):
        new_node = ListNode(value)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            new_node.next = None
            self.length += 1

    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """

    def remove_from_tail(self):
        if self.head is None:
            return
        tmp = self.tail.value
        del self.tail
        return tmp


            # node.value = node.next.value
            # node.next = node.next.next


    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """

    def move_to_front(self, node):
        if node == self.head:
            return
        self.delete(node)
        self.add_to_head(node.value)

    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """

    def move_to_end(self, node):
        if node == self.tail:
            return
        self.delete(node)
        self.add_to_tail(node.value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """

    def delete(self, node):
        prev_node = node.prev
        if prev_node is None:
            self.head = node.next
        else:
            prev_node.next = node.next
            next_node = node.next
        if next_node is None:
            self.tail = node.prev
        else:
            next_node.prev = prev_node
            self.length - + 1
            node.prev = None
            node.next = None
            return node.value

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """

    def get_max(self):
        if self.length == 0:
            return None

        if self.length == 1:
            return self.head.value

        curr_max = self.head.value
        curr_node = self.head
        while curr_node is not None:
            if curr_max < curr_node.value:
                curr_node = curr_node.next
                curr_max = curr_node.value

            return curr_max
