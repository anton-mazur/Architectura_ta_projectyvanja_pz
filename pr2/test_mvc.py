import unittest

from controller import TaskController
from model import TaskModel


class FakeView:
    def __init__(self, titles=None, task_ids=None):
        self.titles = iter(titles or [])
        self.task_ids = iter(task_ids or [])
        self.messages = []
        self.tasks = []

    def show_menu(self):
        pass

    def read_command(self):
        return "0"

    def read_title(self):
        return next(self.titles)

    def read_task_id(self):
        return next(self.task_ids)

    def show_tasks(self, tasks):
        self.tasks = list(tasks)

    def show_message(self, message):
        self.messages.append(message)


class MvcTests(unittest.TestCase):
    def test_model_adds_and_completes_task(self):
        model = TaskModel()
        task = model.add_task("Write documentation")

        self.assertEqual(task.task_id, 1)
        self.assertFalse(task.completed)
        model.complete_task(1)
        self.assertTrue(model.list_tasks()[0].completed)

    def test_controller_coordinates_add_task(self):
        view = FakeView(titles=["Buy milk"])
        controller = TaskController(TaskModel(), view)

        controller.handle("2")

        self.assertEqual(view.messages, ["Added task #1."])
        self.assertEqual(view.tasks, [])

    def test_controller_reports_invalid_completion(self):
        view = FakeView(task_ids=["not-a-number"])
        controller = TaskController(TaskModel(), view)

        controller.handle("3")

        self.assertEqual(view.messages, ["Enter an existing numeric task id."])


if __name__ == "__main__":
    unittest.main()
