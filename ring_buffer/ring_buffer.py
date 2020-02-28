from doubly_linked_list import DoublyLinkedList
# Plan
# The capacity and storage have to be the same length
# whenever the capcity and storage are the same length
# replace the new input with the oldest input
# this could go like first in first out like a que


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.capacity == len(self.storage):
            head = self.storage.head
            while(self.current is not None):

        else:
            self.storage.add_to_head(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        current_node = self.storage.head

        for node in range(self.storage.length):
            list_buffer_contents.append(current_node.value)

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
