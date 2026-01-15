from clearml import Task
task = Task.init(project_name="my project remote", task_name="my task remote")


# This line forces the script to run on a 'default' queue agent
task.execute_remotely(queue_name='default')

# Your training code starts here...
print("This is running on the remote agent!")