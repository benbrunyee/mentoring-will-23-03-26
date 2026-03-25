# =============================================================================
# TO-DO LIST APP (Terminal)
# Concepts: lists, dictionaries, json module, file persistence, while loops,
#           functions, CRUD operations (Create, Read, Update, Delete),
#           menu-driven programs, string formatting
# =============================================================================

import json
import os

SAVE_FILE = "todos.json"


# ---------------------------------------------------------------------------
# File persistence — saving and loading
# ---------------------------------------------------------------------------

def load_todos():
    """
    Load the to-do list from a JSON file.
    If the file doesn't exist yet, return an empty list.
    JSON (JavaScript Object Notation) is a common format for storing data.
    """
    if not os.path.exists(SAVE_FILE):
        return []

    with open(SAVE_FILE, "r") as file:
        return json.load(file)


def save_todos(todos):
    """Save the current to-do list to a JSON file so it persists between runs."""
    with open(SAVE_FILE, "w") as file:
        # indent=2 makes the file human-readable (pretty-printed)
        json.dump(todos, file, indent=2)


# ---------------------------------------------------------------------------
# CRUD operations
# ---------------------------------------------------------------------------

def add_todo(todos):
    """Add a new task to the list."""
    title = input("Task title: ").strip()
    if not title:
        print("Task title cannot be empty.")
        return

    todo = {
        "id": get_next_id(todos),
        "title": title,
        "done": False,
    }

    todos.append(todo)
    save_todos(todos)
    print(f"Added task #{todo['id']}: {title}")


def list_todos(todos):
    """Display all tasks, grouped by status."""
    if not todos:
        print("Your to-do list is empty. Add a task to get started!")
        return

    pending = [t for t in todos if not t["done"]]
    completed = [t for t in todos if t["done"]]

    print(f"\n--- To-Do ({len(pending)} pending, {len(completed)} done) ---")

    if pending:
        print("\nPending:")
        for todo in pending:
            print(f"  [ ] #{todo['id']} {todo['title']}")

    if completed:
        print("\nCompleted:")
        for todo in completed:
            print(f"  [x] #{todo['id']} {todo['title']}")

    print()


def complete_todo(todos):
    """Mark a task as done by its ID."""
    list_todos(todos)

    raw = input("Enter the task ID to mark as complete: ").strip()
    todo = find_todo_by_id(todos, raw)

    if todo is None:
        return

    if todo["done"]:
        print(f"Task #{todo['id']} is already complete.")
        return

    todo["done"] = True
    save_todos(todos)
    print(f"Marked task #{todo['id']} as complete: {todo['title']}")


def delete_todo(todos):
    """Remove a task from the list by its ID."""
    list_todos(todos)

    raw = input("Enter the task ID to delete: ").strip()
    todo = find_todo_by_id(todos, raw)

    if todo is None:
        return

    todos.remove(todo)
    save_todos(todos)
    print(f"Deleted task #{todo['id']}: {todo['title']}")


def clear_completed(todos):
    """Remove all completed tasks at once."""
    completed_count = sum(1 for t in todos if t["done"])

    if completed_count == 0:
        print("No completed tasks to clear.")
        return

    # Keep only tasks that are NOT done
    todos[:] = [t for t in todos if not t["done"]]
    save_todos(todos)
    print(f"Removed {completed_count} completed task(s).")


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def get_next_id(todos):
    """Return an ID one higher than the current maximum."""
    if not todos:
        return 1
    return max(t["id"] for t in todos) + 1


def find_todo_by_id(todos, raw_id):
    """
    Find a to-do by its ID string.
    Returns the dictionary if found, or None if not.
    """
    try:
        target_id = int(raw_id)
    except ValueError:
        print(f"'{raw_id}' is not a valid ID.")
        return None

    for todo in todos:
        if todo["id"] == target_id:
            return todo

    print(f"No task found with ID #{raw_id}.")
    return None


# ---------------------------------------------------------------------------
# Menu
# ---------------------------------------------------------------------------

def show_menu():
    print("What would you like to do?")
    print("  1. List tasks")
    print("  2. Add a task")
    print("  3. Mark a task as complete")
    print("  4. Delete a task")
    print("  5. Clear all completed tasks")
    print("  6. Quit")


def main():
    print("=== To-Do App ===")
    print(f"(Your tasks are saved to '{SAVE_FILE}')\n")

    todos = load_todos()

    while True:
        show_menu()
        choice = input("\nEnter your choice (1-6): ").strip()
        print()

        if choice == "1":
            list_todos(todos)
        elif choice == "2":
            add_todo(todos)
        elif choice == "3":
            complete_todo(todos)
        elif choice == "4":
            delete_todo(todos)
        elif choice == "5":
            clear_completed(todos)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

        print()


if __name__ == "__main__":
    main()
