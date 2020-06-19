from unittest import TestCase
from undo import UndoRedo


class TestUndoRedo(TestCase):

    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)
        self.undoredo = UndoRedo()

    def test_long_list(self):
        # init, Value="None", UndoStack=[], RedoStack=[]
        # SET A, Value="A", UndoStack=[], RedoStack=[]
        self.undoredo.set_value('A')
        # SET B, Value="B", UndoStack=[A], RedoStack=[]
        self.undoredo.set_value('B')
        # UNDO, Value="A", UndoStack=[], RedoStack=[B]
        self.undoredo.undo()
        self.assertEqual('A', self.undoredo.value)
        # REDO, Value="B", UndoStack=[A], RedoStack=[]
        self.undoredo.redo()
        self.assertEqual('B', self.undoredo.value)
        # SET C, Value="C", UndoStack=[A,B], RedoStack=[]
        self.undoredo.set_value('C')
        # REDO, Value="C", UndoStack=[A,B], RedoStack=[]
        new_value = self.undoredo.redo()
        self.assertIsNone(new_value)
        self.assertEqual('C', self.undoredo.value)
        # UNDO, Value="B", UndoStack=[A], RedoStack=[C]
        new_value = self.undoredo.undo()
        self.assertEqual('B', new_value)
        self.assertEqual(1, self.undoredo.undo_stack.depth())
        self.assertEqual('A', self.undoredo.undo_stack.peek())
        self.assertEqual(1, self.undoredo.redo_stack.depth())
        self.assertEqual('C', self.undoredo.redo_stack.peek())
        # SET D, Value="D", UndoStack=[A,B], RedoStack=[C]
        self.undoredo.set_value('D')
        # UNDO, Value="B", UndoStack=[A], RedoStack=[C,D]
        self.undoredo.undo()
        # UNDO, Value="A", UndoStack=[], RedoStack=[C,D,B]
        self.undoredo.undo()
        # UNDO, Value="A", UndoStack=[], RedoStack=[C,D,B]
        self.undoredo.undo()
        # REDO, Value="B", UndoStack=[A], RedoStack=[C,D]
        self.undoredo.redo()
        # REDO, Value="D", UndoStack=[A,B], RedoStack=[C]
        self.undoredo.redo()
        # REDO, Value="C", UndoStack=[A,B,D], RedoStack=[]
        self.undoredo.redo()
        self.assertEqual('C', self.undoredo.value)
        self.assertEqual('[A,B,D]', str(self.undoredo.undo_stack))
        self.assertTrue(self.undoredo.redo_stack.is_empty())
