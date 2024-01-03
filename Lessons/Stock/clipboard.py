clipboard = []
undo_stack = []

def copy(text):
    global clipboard, undo_stack
    undo_stack.append(clipboard.copy())
    clipboard = list(text)

def undo():
    global clipboard, undo_stack
    if undo_stack:
        clipboard = undo_stack.pop()

# Initial content
clipboard = list("01 : Hello, World!")

# Example usage:
print("Current Content:", "".join(clipboard))  # Output: Current Content: Hello, World!

copy("02 : This is a clipboard example.")
print("Current Content:", "".join(clipboard))  # Output: Current Content: This is a clipboard example.

copy("03 : This is another clipboard example.")
print("Current Content:", "".join(clipboard))  # Output: Current Content: This is another clipboard example.

# Undo
undo()
undo()
print("After Undo:", "".join(clipboard))  # Output: After Undo: Hello, World!


