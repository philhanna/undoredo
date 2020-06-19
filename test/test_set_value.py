from unittest import TestCase
from undo import UndoRedo


class TestSetValue(TestCase):

    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)
        self.undoredo = UndoRedo()

    def test_set_value(self):
        self.undoredo.set_value('A')
        self.assertEqual('A', self.undoredo.value)
        self.assertEqual(1, self.undoredo.undo_stack.depth())
        self.assertEqual(0, self.undoredo.redo_stack.depth())

    def test_set_same_value(self):
        self.undoredo.set_value('A')
        expected = (self.undoredo.undo_stack, self.undoredo.redo_stack)
        self.undoredo.set_value('A')
        actual = (self.undoredo.undo_stack, self.undoredo.redo_stack)
        self.assertTrue(expected, actual)
