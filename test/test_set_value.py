from unittest import TestCase
from undo import UndoRedo


class TestSetValue(TestCase):

    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)
        self.undoredo = UndoRedo()

    def test_set_value(self):
        self.undoredo.set_value('A')
        self.assertEqual('A', self.undoredo.value)
        self.assertTrue(self.undoredo.undo_stack.is_empty())
        self.assertTrue(self.undoredo.redo_stack.is_empty())

    def test_set_same_value(self):
        self.undoredo.set_value('A')
        expected = (self.undoredo.undo_stack, self.undoredo.redo_stack)
        self.undoredo.set_value('A')
        actual = (self.undoredo.undo_stack, self.undoredo.redo_stack)
        self.assertTrue(expected, actual)
