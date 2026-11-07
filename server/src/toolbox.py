import random


# 1. Text in -> dictionary out
def analyze_text(text):
    """Return stats about a piece of text."""
    if not isinstance(text, str) or not text.strip():
        raise ValueError("text must be a non-empty string")

    words = text.split()
    letters_only = "".join(c.lower() for c in text if c.isalnum())

    return {
        "characters": len(text),
        "words": len(words),
        "longest_word": max((w.strip(".,!?;:\"'") for w in words), key=len),
        "reversed": text[::-1],
        "is_palindrome": letters_only == letters_only[::-1],
    }


# 2. Number + choice in -> number out
def convert_temperature(value, unit):
    """Convert a temperature. unit is the unit you are converting FROM: 'C' or 'F'."""
    try:
        value = float(value)
    except (TypeError, ValueError):
        raise ValueError("value must be a number")

    unit = str(unit).upper()
    if unit == "C":
        return {"input": f"{value} C", "output": f"{value * 9 / 5 + 32:.1f} F"}
    if unit == "F":
        return {"input": f"{value} F", "output": f"{(value - 32) * 5 / 9:.1f} C"}
    raise ValueError("unit must be 'C' or 'F'")


def roll_dice(sides=6, count=1):
    """Roll `count` dice with `sides` sides each."""
    try:
        sides, count = int(sides), int(count)
    except (TypeError, ValueError):
        raise ValueError("sides and count must be whole numbers")

    if not 2 <= sides <= 100:
        raise ValueError("sides must be between 2 and 100")
    if not 1 <= count <= 20:
        raise ValueError("count must be between 1 and 20")

    rolls = [random.randint(1, sides) for _ in range(count)]
    return {"rolls": rolls, "total": sum(rolls)}


class TodoList:
    """An in-memory to-do list. Data resets when the program restarts."""

    def __init__(self):
        self._items = []
        self._next_id = 1

    def add(self, title):
        if not isinstance(title, str) or not title.strip():
            raise ValueError("title must be a non-empty string")
        item = {"id": self._next_id, "title": title.strip(), "done": False}
        self._items.append(item)
        self._next_id += 1
        return item

    def all(self):
        return list(self._items)

    def complete(self, item_id):
        item = self._find(item_id)
        item["done"] = True
        return item

    def remove(self, item_id):
        item = self._find(item_id)
        self._items.remove(item)
        return item

    def _find(self, item_id):
        for item in self._items:
            if item["id"] == item_id:
                return item
        raise KeyError(f"no item with id {item_id}")


def main():
    todos = TodoList()
    menu = """
        1) Analyze text
        2) Convert temperature
        3) Roll dice
        4) Add to-do
        5) Show to-dos
        q) Quit
    """
    while True:
        print(menu)
        choice = input("Choose: ").strip().lower()
        try:
            if choice == "1":
                print(analyze_text(input("Text: ")))
            elif choice == "2":
                print(convert_temperature(input("Value: "), input("From (C/F): ")))
            elif choice == "3":
                sides = input("Sides: ") or 6
                cnt = input("How many: ") or 1
                print(roll_dice(sides,cnt))
            elif choice == "4":
                print(todos.add(input("Task: ")))
            elif choice == "5":
                print(todos.all())
            elif choice == "q":
                break
            else:
                print("Unknown option")
        except ValueError as err:
            print(f"Error: {err}")


# Terminal CLI 
if __name__ == "__main__":
    main()
