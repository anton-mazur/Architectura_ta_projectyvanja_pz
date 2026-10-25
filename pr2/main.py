"""Application entry point."""

from controller import TaskController
from model import TaskModel
from view import ConsoleView


if __name__ == "__main__":
    TaskController(TaskModel(), ConsoleView()).run()
