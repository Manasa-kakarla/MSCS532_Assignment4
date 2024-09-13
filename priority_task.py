class MaxHeap:
    def __init__(self):
        self.heap = []
        self.task_index_map = {}  # Maps task IDs to their index in the heap

    def insert(self, task):
        self.heap.append(task)
        self.task_index_map[task.task_id] = len(self.heap) - 1
        self._heapify_up(len(self.heap) - 1)

    def remove_max(self):
        if len(self.heap) == 0:
            raise IndexError("remove_max from an empty heap")

        max_task = self.heap[0]
        last_task = self.heap.pop()
        if len(self.heap) > 0:
            self.heap[0] = last_task
            self.task_index_map[last_task.task_id] = 0
            self._heapify_down(0)
        
        del self.task_index_map[max_task.task_id]
        return max_task

    def update_priority(self, task_id, new_priority):
        """
        Update the priority of a task and adjust its position in the heap.

        :param task_id: The ID of the task whose priority is to be updated.
        :param new_priority: The new priority of the task.
        """
        if task_id not in self.task_index_map:
            raise KeyError(f"Task ID {task_id} not found in heap")
        
        index = self.task_index_map[task_id]
        old_priority = self.heap[index].priority
        self.heap[index].priority = new_priority

        if new_priority > old_priority:
            self._heapify_up(index)
        elif new_priority < old_priority:
            self._heapify_down(index)

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self.task_index_map[self.heap[index].task_id] = index
            self.task_index_map[self.heap[parent_index].task_id] = parent_index
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        largest = index
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2

        if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
            largest = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
            largest = right_child_index

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.task_index_map[self.heap[index].task_id] = index
            self.task_index_map[self.heap[largest].task_id] = largest
            self._heapify_down(largest)

    def __repr__(self):
        return repr(self.heap)
