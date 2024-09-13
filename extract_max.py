class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, task):
        self.heap.append(task)
        self._heapify_up(len(self.heap) - 1)

    def remove_max(self):
        """
        Remove and return the task with the highest priority (root of the heap).
        """
        if len(self.heap) == 0:
            raise IndexError("remove_max from an empty heap")

        # Swap the root with the last element
        max_task = self.heap[0]
        last_task = self.heap.pop()  # Remove the last element
        if len(self.heap) > 0:
            self.heap[0] = last_task  # Move the last element to the root
            self._heapify_down(0)  # Restore the heap property

        return max_task

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            # Swap the current element with its parent
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            # Recursively heapify the parent
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        largest = index
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        # Check if left child exists and is greater than the current node
        if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
            largest = left_child_index

        # Check if right child exists and is greater than the current node
        if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
            largest = right_child_index

        # If the largest is not the current node, swap and continue heapifying
        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def __repr__(self):
        return repr(self.heap)
