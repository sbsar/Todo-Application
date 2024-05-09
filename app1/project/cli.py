#Author Saim
from functions import *
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is ",now)


while True:
    action_item = input("Add, Show, Edit, Remove or Exit ").strip()
    if "add" in action_item:
        todo = action_item[4:] + "\n"
        todos = get_todos("todos.txt")

        todos.append(f"{now} - {todo}")
        write_todos("todos.txt", todos)

    elif "show" in action_item:
        todos = get_todos("todos.txt")
        # new_items = [i.strip("\n") for i in todos]
        for index, items in enumerate(todos):
            items = items.strip("\n")
            row = f"{index + 1}-{items}"
            print(row)

    # elif "edit" in action_item:
    #     word_input = action_item[5:] + "\n"
    #
    #     if word_input in todos:
    #         ind = todos.index(word_input)
    #         new_word = input("Enter the new word : ").strip()
    #         todos[ind] = new_word + "\n"
    #         with open("todos.txt", "w") as file:
    #             file.writelines(todos)
    #     else:
    #         print("Invalid word does not exists")
    elif "edit" in action_item:
        try:
            word_input = action_item[5:] + "\n"
            print(word_input)
            num = int(word_input) - 1
            new_todo = input("Enter new todo : ")
            todos = get_todos("todos.txt")
            todos[num] = f"{now} - {new_todo}" + "\n"
            write_todos("todos.txt", todos)
        except ValueError:
            print("Invalid Entry")
            # action_item = input("Add, Show, Edit, Remove or Exit ").strip()
            continue
        except IndexError:
            print("Out of Range")
            # action_item = input("Add, Show, Edit, Remove or Exit ").strip()
            continue


    elif "remove" in action_item:

        # todos = [i for i in todos]
        word_input = action_item[6:].strip() + "\n"
        print(word_input)
        todos = get_todos("todos.txt")
        if word_input in todos:
            ind = todos.index(word_input)
            todos.pop(ind)
            write_todos("todos.txt", todos)
        else:
            print("Invalid word does not exists")
    elif "exit" in action_item:
        break
    else:
        print("Try again")
print("Done for now ")
