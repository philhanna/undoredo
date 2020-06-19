from unittest import TestCase
from undo import UndoRedo


class TestRedo(TestCase):

    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)
        self.undoredo = UndoRedo()

    def test_redo(self):
        self.undoredo.set_value('A')
        self.assertEqual('A', self.undoredo.value)
        self.assertListEqual([None], self.undoredo.undo_stack.stack)
        self.assertListEqual([], self.undoredo.redo_stack.stack)

        self.undoredo.set_value('B')
        self.assertEqual('B', self.undoredo.value)
        self.assertListEqual([None, 'A'], self.undoredo.undo_stack.stack)
        self.assertListEqual([], self.undoredo.redo_stack.stack)

        self.undoredo.undo()
        self.assertEqual('A', self.undoredo.value)
        self.assertListEqual([None], self.undoredo.undo_stack.stack)
        self.assertListEqual(['B'], self.undoredo.redo_stack.stack)

        self.undoredo.redo()
        self.assertEqual('B', self.undoredo.value)
        self.assertListEqual([None, 'A'], self.undoredo.undo_stack.stack)
        self.assertListEqual([], self.undoredo.redo_stack.stack)
        self.assertTrue(self.undoredo.redo_stack.is_empty())
