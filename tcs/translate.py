import itertools
import mido
from tcs import notes
from tcs.instructions import *

# Borrowed from Unrelated's translator
class TrackPlayer:

    def __init__(self, track):
        self.iterator = iter(track)
        self.ticks = 0
        self.done = False
        self.next_message = None
    
    def step(self, n = 1):
        self.ticks -= n

    def messages(self):
        if self.ticks <= 0 and not self.done:
            if self.next_message:
                yield self.next_message
            try:
                self.next_message = next(self.iterator)
                self.ticks += self.next_message.time
                yield from self.messages()
            except StopIteration:
                self.done = True

def translate(midi):
    print("Charging flux capacitors")
    players = [TrackPlayer(track) for track in midi.tracks]
    #d = list(midi)
    #print("We've got {} messages to translate".format(len(d)))
    result = [SpeedInstruction(Mode.SET, 120)] # Default bpm
    oldVelocity = 64
    i = set()
    while not all(p.done for p in players):
        control = 1
        for message in itertools.chain.from_iterable(p.messages() for p in players):
            if message.type == "note_on":
                pitch = message.note - 69 # assuming the base is 'concert a'
                if message.velocity != oldVelocity:
                    oldVelocity = message.velocity
                    volume = message.velocity / 64
                    result.append(VolumeInstruction(Mode.SET, volume*100))
                result.append(NoteInstruction(notes.MIDI_TO_SFX[control], pitch))
                result.append(CombineInstruction())
            elif message.type == 'set_tempo':
                bpm = mido.tempo2bpm(message.tempo)
                result.append(SpeedInstruction(Mode.SET, bpm))
            elif message.type == "control_change":
                control = message.control

        step = min((p.ticks for p in players if not p.done), default=0)
        beats = step / midi.ticks_per_beat
        result.append(PauseInstruction(beats))

        for p in players:
            p.step(step)
            
    print("OK, done")

    return result