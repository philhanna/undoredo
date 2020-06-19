from unittest import TestCase
from undo import UndoRedo


class TestRedo(TestCase):

    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)
        self.undoredo = UndoRedo()

    def test_redo(self):
        self.undoredo.set_value('A')
        self.undoredo.set_value('B')
        new_value = self.undoredo.undo()
        self.assertEqual('A', new_value)
        new_value = self.undoredo.redo()
        self.assertEqual('B', new_value)
        self.assertEqual('B', self.undoredo.value)
        self.assertEqual(['A'], self.undoredo.undo_stack.stack)
        self.assertTrue(self.undoredo.redo_stack.is_empty())
