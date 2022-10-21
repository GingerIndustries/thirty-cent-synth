import argparse
import mido
from tcs import translate

parser = argparse.ArgumentParser(prog="tcs", description="Thirty Cent Synth: Translate a MIDI file to THIRTY DOLLAR FORMAT")
parser.add_argument("input", help="The input MIDI file")

def main():
    args = parser.parse_args()
    print("Target file:", args.input)
    print("Output will be in", args.input + ".🗿")
    result = translate.translate(mido.MidiFile(args.input))
    print("Saving...")
    with open(args.input + ".🗿", "w") as f:
        f.write("|".join([repr(x) for x in result]))

if __name__ == "__main__":
    main()