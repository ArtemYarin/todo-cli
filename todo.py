class TodoList:
    def __init__(self):
        self.todos = ['buy']


    def add(self, todo):
        self.todos.append(todo)


    def delete(self, todoToDel):
        try:
            self.todos.remove(todoToDel)
        except ValueError:
            print(f"There isn't {todoToDel} in your todo list")


    def update(self, todoToChange, newTodo):
        try:
            index = self.todos.index(todoToChange)
        except Exception:
            print(f"There isn't {todoToChange} in your todo list")
        else:
            self.todos[index] = newTodo


    def get(self):
        if self.todos:
            i = 1
            for todo in self.todos:
                print(i, todo)
                i += 1
        else:
            print("You don't have any todos yet.")



# Start
todoList = TodoList()
print('Welcome')
while True:
    print('Choose an action: ')
    action = input()

    match action:
        case 'get':
            todoList.get()
        case 'add':
            newTodo = input('New todo: ')
            todoList.add(newTodo)
        case 'update':
            oldTodo = input('Old todo: ')
            newTodo = input('New todo: ')
            todoList.update(oldTodo, newTodo)
        case 'delete':
            todo = input('Todo to delete: ')
            todoList.delete(todo)
        case 'exit':
            break
    print()
