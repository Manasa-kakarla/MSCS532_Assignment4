import heapq

# Initialize an empty priority queue
priority_queue = []

# Function to check if the priority queue is empty
def is_empty(pq):
    return len(pq) == 0

# Example usage
print(is_empty(priority_queue))  # True, as the priority queue is empty

# Push elements onto the priority queue
heapq.heappush(priority_queue, (1, 'task1'))
heapq.heappush(priority_queue, (2, 'task2'))

print(is_empty(priority_queue))  # False, as there are elements in the priority queue

# Pop elements from the priority queue
print(heapq.heappop(priority_queue))  # (1, 'task1')
print(heapq.heappop(priority_queue))  # (2, 'task2')

print(is_empty(priority_queue))  # True, as all elements have been removed
