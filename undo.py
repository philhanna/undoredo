class UndoRedo:
    """ Provides coordinated support for undo and redo """

    def __init__(self):
        self.value = None
        self.undo_stack = Stack()
        self.redo_stack = Stack()

    def set_value(self, new_value):
        if self.value is not None:
            if self.value != new_value:
                self.undo_stack.push(self.value)
        self.value = new_value
        return self.value

    def undo(self):
        if self.undo_stack.is_empty():
            return None
        if self.value is not None:
            self.redo_stack.push(self.value)
        new_value = self.undo_stack.pop()
        self.value = new_value
        return self.value

    def redo(self):
        if self.redo_stack.is_empty():
            return None
        if self.value is not None:
            self.undo_stack.push(self.value)
        new_value = self.redo_stack.pop()
        self.value = new_value
        return self.value

    def __str__(self):
        sb = f'value="{self.value}", undo_stack={self.undo_stack}, redo_stack={self.redo_stack}'
        return sb


class Stack:
    """ A stack used for undo or redo
    """

    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        x = None
        if not self.is_empty():
            x = self.stack.pop()
        return x

    def peek(self):
        x = None
        if not self.is_empty():
            x = self.stack[-1]
        return x

    def depth(self):
        return len(self.stack)

    def is_empty(self):
        return self.depth() == 0

    def __str__(self):
        innards = ",".join(self.stack)
        return f'[{innards}]'
