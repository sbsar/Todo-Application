def get_todos(filepath):
    """
    The function reads the file
    and returns the list of
    todo items
    """
    with open(filepath, "r") as file:
        todos = file.readlines()
    return todos

print(help(get_todos))
def write_todos(filepath, todos_arg):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")

