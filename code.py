"""
This script demonstrates a basic program to manage tasks in a to-do list.
"""

from typing import List


class TaskManager:
    """Class to manage a list of tasks."""

    def __init__(self):
        """Initialize the TaskManager with an empty task list."""
        self.tasks: List[str] = []

    def add_task(self, task: str) -> None:
        """
        Add a task to the list.

        Args:
            task (str): The task to be added.
        """
        if not task:
            raise ValueError("Task cannot be empty")
        self.tasks.append(task)
        print(f"Task added: {task}")

    def remove_task(self, task: str) -> None:
        """
        Remove a task from the list.

        Args:
            task (str): The task to be removed.
        """
        try:
            self.tasks.remove(task)
            print(f"Task removed: {task}")
        except ValueError:
            print(f"Task not found: {task}")

    def display_tasks(self) -> None:
        """Display all tasks in the list."""
        if not self.tasks:
            print("No tasks available.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")


def main():
    """Main function to test the TaskManager."""
    manager = TaskManager()
    manager.add_task("Complete homework")
    manager.add_task("Read a book")
    manager.display_tasks()
    manager.remove_task("Complete homework")
    manager.display_tasks()


if __name__ == "__main__":
    main()
