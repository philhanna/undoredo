#! /usr/bin/python3
import sys

try:
    from undo import UndoRedo
except:
    sys.path.append("..")
    from undo import UndoRedo


class Mainline:
    """ Demonstrates an undo/redo session """

    def __init__(self):
        """ Creates the undoer """
        self.app = UndoRedo()

    def run(self):
        """ Runs the session """

        history = []
        logentry = "init"

        while True:

            # Log the current status
            status = str(self.app)
            logentry = logentry + ", " + status
            history.append(logentry)

            # Prompt for input
            print(status)
            print("> ", end='')
            line = input()

            # Quit
            if line.upper().startswith("Q"):
                break

            # Get the input tokens, ignoring blank lines
            logentry = line
            tokens = line.split()
            if len(tokens) == 0:
                continue

            # First token is the command (set, undo, redo, help)
            first = tokens[0].upper()

            # Help
            if first.startswith("H"):
                pass

            # Set
            elif first.startswith("S"):
                if len(tokens) < 2:
                    print("Set to what?")
                    continue
                value_to_set = tokens[1]
                self.app.set_value(value_to_set)

            # Undo
            elif first.startswith("U"):
                self.app.undo()

            # Redo
            elif first.startswith("R"):
                self.app.redo()

            # Unrecognized command
            else:
                print(f'"{line}" ?')

        # At end, print the history of this session
        for status in history:
            print(status)


#   ============================================================
#   Mainline
#   ============================================================
if __name__ == '__main__':
    m = Mainline()
    m.run()
