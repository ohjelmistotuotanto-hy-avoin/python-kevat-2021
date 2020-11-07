from todo import Todo


class TodoRepository:
    def __init__(self):
        self.todos = []

    def find_all(self):
        return self.todos

    def find_by_username(self, username):
        todos = self.find_all()

        user_todos = filter(
            lambda todo: todo.user and todo.user.username == username,
            todos
        )

        return list(user_todos)

    def find_by_id(self, todo_id):
        todos = self.find_all()

        todos_with_id = filter(
            lambda todo: todo.id == todo_id,
            todos
        )

        todos_with_id_list = list(todos_with_id)

        return todos_with_id_list[0] if len(todos_with_id_list) > 0 else None

    def create(self, todo):
        todos = self.find_all()

        existing_todos = filter(
            lambda t: t.id == todo.id,
            todos
        )

        if len(list(existing_todos)) > 0:
            raise Exception(f"Todo with id {todo.id} already exists")

        todos.append(todo)

        self.todos = todos

        return todo

    def delete(self, todo_id):
        todos = self.find_all()

        todos_without_id = filter(lambda todo: todo.id != todo_id, todos)

        self.todos = list(todos_without_id)

    def delete_all(self):
        self.todos = []


todo_repository = TodoRepository()
