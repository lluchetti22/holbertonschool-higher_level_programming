class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        items = list(items)  # Consume iterator once, reuse for both len and super
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)


# Testing
vl = VerboseList()

vl.append(1)            # Added [1] to the list.
vl.append(2)            # Added [2] to the list.
vl.append(3)            # Added [3] to the list.
vl.extend([4, 5, 6])    # Extended the list with [3] items.
vl.remove(3)            # Removed [3] from the list.
vl.pop()                # Popped [6] from the list.
vl.pop(0)               # Popped [1] from the list.

print(vl)               # [2, 4, 5]
