tasks = []


def show_tasks():
    print("Lista de tareas:")
    for idx, task in enumerate(tasks):
        print(f"{idx + 1}.{task}")

def add_task(task):
    tasks.append(task)
    print("Tarea " + task +" agregada.")

def remove_task(idx):
    if 0 <= idx < len(tasks):
        removed = tasks.pop(idx)
        print("Tarea "+ removed + " eliminada.")
    else:
        print("Indice invalido")

# Ejemplo de uso
add_task("Estudiar Python")
add_task("Ir al trabajo")
show_tasks()
remove_task(1)
show_tasks()