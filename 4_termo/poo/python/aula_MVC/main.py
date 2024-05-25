from model import TaskModel
from view import TaskView
from controller import TaskController

model = TaskModel()
view = TaskView()
controller = TaskController(model, view)

controller.add_task("Terminar tarefa")
controller.add_task("Preparar apresentação")

controller.update_view()