class Task:
    def __init__(self, task_id, priority, arrival_time, deadline, description=""):
        """
        Initialize a new Task.

        :param task_id: Unique identifier for the task.
        :param priority: Priority of the task (higher value means higher priority).
        :param arrival_time: Time when the task arrives (e.g., timestamp or an integer).
        :param deadline: Deadline by which the task needs to be completed.
        :param description: Optional description of the task.
        """
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline
        self.description = description

    def __repr__(self):
        """
        Return a string representation of the task for debugging and printing.
        """
        return (f"Task(task_id={self.task_id}, priority={self.priority}, "
                f"arrival_time={self.arrival_time}, deadline={self.deadline}, "
                f"description='{self.description}')")

    def __lt__(self, other):
        """
        Define comparison for sorting tasks by priority.
        Tasks with higher priority should come first.
        """
        if self.priority == other.priority:
            return self.arrival_time < other.arrival_time
        return self.priority > other.priority

    def __eq__(self, other):
        """
        Define equality for tasks.
        """
        return (self.task_id == other.task_id and
                self.priority == other.priority and
                self.arrival_time == other.arrival_time and
                self.deadline == other.deadline and
                self.description == other.description)

    def is_due(self, current_time):
        """
        Check if the task is due based on the current time.

        :param current_time: The current time to check against the deadline.
        :return: True if the current time is past the deadline, otherwise False.
        """
        return current_time > self.deadline

# Example usage:
task1 = Task(task_id=1, priority=10, arrival_time=5, deadline=20, description="Task 1")
task2 = Task(task_id=2, priority=20, arrival_time=10, deadline=15, description="Task 2")

print(task1)
print(task2)

# List of tasks
tasks = [task1, task2]
# Sorting tasks based on priority and arrival time
tasks.sort()
print("Sorted tasks:", tasks)

# Check if a task is due
print("Is task1 due?", task1.is_due(current_time=25))
