from enum import Enum

class Mode(Enum):
    SET = ""
    ADD = "+"
    MULTIPLY = "x"

class Instruction:
    def __init__(self, name, args):
        self.name = name
        self.args = args
    def __repr__(self):
        return self.name + ("@" + "@".join(map(str, self.args)) if self.args else "")

class NoteInstruction(Instruction):
    def __init__(self, note, pitch):
        super().__init__(note.value, [pitch])

class SpeedInstruction(Instruction):
    def __init__(self, mode, speed):
        super().__init__("!speed", [speed] + ([mode.value] if mode.value else []))
class VolumeInstruction(Instruction):
    def __init__(self, mode, volume):
        super().__init__("!volume", [volume] + ([mode.value] if mode.value else []))

class PauseInstruction(Instruction):
    def __init__(self, beats):
        super().__init__("!stop", [beats])
class TransposeInstruction(Instruction):
    def __init__(self, mode, pitch):
        super().__init__("!transpose", [pitch] + [mode.value] if mode.value else [])
        if mode == Mode.MULTIPLY:
            raise ValueError("Cannot use multiply mode with transpose")

class StopAllInstruction(Instruction):
    def __init__(self):
        super().__init__("!cut", [])
class CombineInstruction(Instruction):
    def __init__(self):
        super().__init__("!combine", [])
class SeparatorInstruction(Instruction):
    def __init__(self):
        super().__init__("!divider", [])