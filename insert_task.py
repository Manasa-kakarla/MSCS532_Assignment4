class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, task):
        """
        Insert a new task into the heap and maintain the heap property.

        :param task: Task instance to be inserted.
        """
        self.heap.append(task)  # Add the new task to the end of the heap
        self._heapify_up(len(self.heap) - 1)  # Restore heap property

    def _heapify_up(self, index):
        """
        Restore the heap property by bubbling up the element at the given index.

        :param index: The index of the element to be bubbled up.
        """
        parent_index = (index - 1) // 2

        if index > 0 and self.heap[index] > self.heap[parent_index]:
            # Swap the current element with its parent
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            # Recursively heapify the parent
            self._heapify_up(parent_index)

    def __repr__(self):
        """
        Return a string representation of the heap.
        """
        return repr(self.heap)
