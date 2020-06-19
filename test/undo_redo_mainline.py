#! /usr/bin/python3
import sys

try:
    from undo import UndoRedo
except:
    sys.path.append("..")
    from undo import UndoRedo


class Mainline:

    def __init__(self):
        self.app = UndoRedo()

    def run(self):
        history = []
        logentry = "init"
        while True:
            status = str(self.app)
            logentry = logentry + ", " + status
            history.append(logentry)
            print(status)
            print("> ", end='')
            line = input().upper()
            if line.startswith("Q"):
                break
            logentry = line
            tokens = line.split()
            if len(tokens) == 0:
                continue
            first = tokens[0][0]
            if first == "S":
                if len(tokens) < 2:
                    print("Set to what?")
                    continue
                value_to_set = tokens[1]
                self.app.set_value(value_to_set)
            elif first == "U":
                self.app.undo()
            elif first == "R":
                self.app.redo()
            else:
                print(f'"{line}" ?')
        for status in history:
            print(status)


#   ============================================================
#   Mainline
#   ============================================================
if __name__ == '__main__':
    m = Mainline()
    m.run()
