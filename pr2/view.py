"""View layer for the task manager example."""

from collections.abc import Iterable

from model import Task


class ConsoleView:
    """Renders output and reads commands; it contains no business rules."""

    def show_menu(self) -> None:
        print("\nTask Manager")
        print("1. List tasks")
        print("2. Add task")
        print("3. Complete task")
        print("0. Exit")

    def read_command(self) -> str:
        return input("Choose an action: ").strip()

    def read_title(self) -> str:
        return input("Task title: ")

    def read_task_id(self) -> str:
        return input("Task id: ").strip()

    def show_tasks(self, tasks: Iterable[Task]) -> None:
        tasks = list(tasks)
        if not tasks:
            print("No tasks yet.")
            return
        for task in tasks:
            status = "x" if task.completed else " "
            print(f"[{status}] {task.task_id}: {task.title}")

    def show_message(self, message: str) -> None:
        print(message)
