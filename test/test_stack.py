from unittest import TestCase

from undo import Stack


class TestUndoStack(TestCase):

    def test_push(self):
        stack = Stack()
        stack.push('A')
        self.assertEqual(1, stack.depth())

    def test_peek(self):
        stack = Stack()
        stack.push('B')
        self.assertEqual(1, stack.depth())
        self.assertEqual('B', stack.peek())
        self.assertEqual(1, stack.depth())

    def test_pop(self):
        stack = Stack()
        stack.push('B')
        self.assertEqual(1, stack.depth())
        self.assertEqual('B', stack.pop())
        self.assertEqual(0, stack.depth())
