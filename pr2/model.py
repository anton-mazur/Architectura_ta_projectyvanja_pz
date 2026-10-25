"""Model layer for the task manager example."""

from dataclasses import dataclass


@dataclass
class Task:
    """A task and its current state."""

    task_id: int
    title: str
    completed: bool = False


class TaskModel:
    """Stores tasks and exposes business operations without UI concerns."""

    def __init__(self) -> None:
        self._tasks: list[Task] = []
        self._next_id = 1

    def add_task(self, title: str) -> Task:
        normalized_title = title.strip()
        if not normalized_title:
            raise ValueError("Task title cannot be empty")

        task = Task(self._next_id, normalized_title)
        self._tasks.append(task)
        self._next_id += 1
        return task

    def list_tasks(self) -> list[Task]:
        return list(self._tasks)

    def complete_task(self, task_id: int) -> Task:
        for task in self._tasks:
            if task.task_id == task_id:
                task.completed = True
                return task
        raise KeyError(task_id)
