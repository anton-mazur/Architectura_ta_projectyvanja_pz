"""Controller layer coordinating the model and the view."""

from model import TaskModel
from view import ConsoleView


class TaskController:
    """Translates user actions into model operations and view updates."""

    def __init__(self, model: TaskModel, view: ConsoleView) -> None:
        self.model = model
        self.view = view

    def run(self) -> None:
        while True:
            self.view.show_menu()
            command = self.view.read_command()
            if command == "0":
                self.view.show_message("Goodbye!")
                return
            self.handle(command)

    def handle(self, command: str) -> None:
        if command == "1":
            self.view.show_tasks(self.model.list_tasks())
        elif command == "2":
            self._add_task()
        elif command == "3":
            self._complete_task()
        else:
            self.view.show_message("Unknown action.")

    def _add_task(self) -> None:
        try:
            task = self.model.add_task(self.view.read_title())
        except ValueError as error:
            self.view.show_message(str(error))
        else:
            self.view.show_message(f"Added task #{task.task_id}.")

    def _complete_task(self) -> None:
        try:
            task_id = int(self.view.read_task_id())
            task = self.model.complete_task(task_id)
        except (ValueError, KeyError):
            self.view.show_message("Enter an existing numeric task id.")
        else:
            self.view.show_message(f"Completed task #{task.task_id}.")
