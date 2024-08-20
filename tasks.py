tasks = []
task_id_counter = 1

def add_task(title, description=""):
    global task_id_counter
    task = {
        "id": task_id_counter,
        "title": title,
        "description": description
    }
    tasks.append(task)
    task_id_counter += 1
    return task


def get_tasks():
    return tasks


def get_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return None


def update_task(task_id, title=None, description=None):
    task = get_task(task_id)
    if task:
        if title:
            task["title"] = title
        if description:
            task["description"] = description
    return task


def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] != task_id]