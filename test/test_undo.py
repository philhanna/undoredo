from unittest import TestCase
from undo import UndoRedo


class TestUndo(TestCase):

    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)
        self.undoredo = UndoRedo()

    def test_undo(self):
        self.undoredo.set_value('A')
        self.undoredo.set_value('B')
        new_value = self.undoredo.undo()
        self.assertEqual('A', new_value)
        self.assertEqual('A', self.undoredo.value)
        self.assertTrue(self.undoredo.undo_stack.is_empty())
        self.assertEqual(['B'], self.undoredo.redo_stack.stack)

    def test_undo_empty(self):
        self.undoredo.set_value('A')
        self.assertTrue(self.undoredo.undo_stack.is_empty())
        self.assertTrue(self.undoredo.redo_stack.is_empty())
        new_value = self.undoredo.undo()
        self.assertIsNone(new_value)
