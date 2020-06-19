from unittest import TestCase
from undo import UndoRedo


class TestUndoRedo(TestCase):

    def __init__(self, *args, **kwargs):
        TestCase.__init__(self, *args, **kwargs)
        self.undoredo = UndoRedo()

    def test_long_list(self):
        ur = self.undoredo

        ur.set_value('A')
        self.assertEqual('A', ur.value)
        self.assertListEqual([None], ur.undo_stack.stack)
        self.assertListEqual([], ur.redo_stack.stack)

        ur.set_value('B')
        self.assertEqual('B', ur.value)
        self.assertListEqual([None, 'A'], ur.undo_stack.stack)
        self.assertListEqual([], ur.redo_stack.stack)

        ur.undo()
        self.assertEqual('A', ur.value)
        self.assertListEqual([None], ur.undo_stack.stack)
        self.assertListEqual(['B'], ur.redo_stack.stack)

        ur.redo()
        self.assertEqual('B', ur.value)
        self.assertListEqual([None, 'A'], ur.undo_stack.stack)
        self.assertListEqual([], ur.redo_stack.stack)

        ur.set_value('C')
        self.assertEqual('C', ur.value)
        self.assertListEqual([None, 'A', 'B'], ur.undo_stack.stack)
        self.assertListEqual([], ur.redo_stack.stack)

        ur.redo()
        self.assertEqual('C', ur.value)
        self.assertListEqual([None, 'A', 'B'], ur.undo_stack.stack)
        self.assertListEqual([], ur.redo_stack.stack)

        ur.undo()
        self.assertEqual('B', ur.value)
        self.assertListEqual([None, 'A'], ur.undo_stack.stack)
        self.assertListEqual(['C'], ur.redo_stack.stack)

        ur.set_value('D')
        self.assertEqual('D', ur.value)
        self.assertListEqual([None, 'A', 'B'], ur.undo_stack.stack)
        self.assertListEqual(['C'], ur.redo_stack.stack)

        ur.undo()
        self.assertEqual('B', ur.value)
        self.assertListEqual([None, 'A'], ur.undo_stack.stack)
        self.assertListEqual(['C', 'D'], ur.redo_stack.stack)

        ur.undo()
        self.assertEqual('A', ur.value)
        self.assertListEqual([None], ur.undo_stack.stack)
        self.assertListEqual(['C', 'D', 'B'], ur.redo_stack.stack)

        ur.undo()
        self.assertEqual(None, ur.value)
        self.assertListEqual([], ur.undo_stack.stack)
        self.assertListEqual(['C', 'D', 'B', 'A'], ur.redo_stack.stack)

        ur.redo()
        self.assertEqual('A', ur.value)
        self.assertListEqual([None], ur.undo_stack.stack)
        self.assertListEqual(['C', 'D', 'B'], ur.redo_stack.stack)

        ur.redo()
        self.assertEqual('B', ur.value)
        self.assertListEqual([None, 'A'], ur.undo_stack.stack)
        self.assertListEqual(['C', 'D'], ur.redo_stack.stack)

        ur.redo()
        self.assertEqual('D', ur.value)
        self.assertListEqual([None, 'A', 'B'], ur.undo_stack.stack)
        self.assertListEqual(['C'], ur.redo_stack.stack)
