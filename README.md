Priority Queue Using Heaps
This project provides implementations of priority queues using max-heap data structures. It includes the following functionalities:

Inserting tasks into the heap.
Removing the highest/lowest priority task.
Modifying the priority of existing tasks.
Checking if the heap is empty.

'heap_sort.py': contains max-heap building
'class_task.py': contains class task to represent individual tasks, like task id, dedline, arrival time, etc.
'insert_task.py': contains the logic to represent a new task into the heap.
'extract_max.py': contains the logic to remove and return the task with higher priority from the heap.
'priority_task.py': contains the logic to modify the priority of an existing task in the heap.
'empty_queue.py': contains the check to determine if the priority queue is empty.

prerequisites:
python3.x

Run the code:
To run above files below are the commands:
python heap_sort.py
python class_task.py
python insert_task.py
python extract_max.py
python priority_task.py
python empty_queue.py

Sample output for heap_sort.py:
python -u "/home/manasa/vscode_projects/heap_implementation/heap_sort.py"
Sorted array is: [5, 6, 7, 11, 12, 13]
sample output for class_task.py:
python -u "/home/manasa/vscode_projects/heap_implementation/class_task.py"
Task(task_id=1, priority=10, arrival_time=5, deadline=20, description='Task 1')
Task(task_id=2, priority=20, arrival_time=10, deadline=15, description='Task 2')
Sorted tasks: [Task(task_id=2, priority=20, arrival_time=10, deadline=15, description='Task 2'), Task(task_id=1, priority=10, arrival_time=5, deadline=20, description='Task 1')]
Is task1 due? True
sample output for empty_queue.py:
python -u "/home/manasa/vscode_projects/heap_implementation/empty_queue.py"
True
False
(1, 'task1')
(2, 'task2')
True

summary of findimgs:
Heap Operations: The implementations provide efficient heap operations with logarithmic time complexity for insertion, removal, and priority adjustment.
Max-Heap: Ensures that the maximum priority element is always at the root. Supports priority modifications and checks for heap emptiness
Error Handling: Both heap implementations handle cases where operations are performed on an empty heap, raising appropriate exceptions.

Feel free to contribute by submitting issues or pull requests. Your contributions to improving the heap implementations are welcome.
This project is licensed under the MIT License - see the LICENSE file for details.
