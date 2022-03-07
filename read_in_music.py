from music21 import converter, instrument, note, chord
import os

# Midi website: https://www.midiworld.com/

def convert_to_music21(dataset_path):
    
    notes = []
    
    for file in os.listdir(dataset_path):
        print(file)
        music_object = converter.parse(dataset_path + "/" + file)    
        notes_to_parse = None
        
        parts = instrument.partitionByInstrument(music_object)
        if parts: # file has instrument parts
            notes_to_parse = parts.parts[0].recurse()
        else: # file has notes in a flat structure
            notes_to_parse = music_object.flat.notes
        for element in notes_to_parse:
            if isinstance(element, note.Note):
                notes.append(str(element.pitch))
            elif isinstance(element, chord.Chord):
                notes.append('.'.join(str(n) for n in element.normalOrder))

    return notes

# Get all the notes that are in the dataset
all_notes = convert_to_music21("dataset")
# Convert the notes to a set of all the pitch names that exist
pitch_names = sorted(set(all_notes))
# Create a dictionary to map pitches to integers (0 - n notes)
# {note: int value, ...}
note_to_int = dict((note, number) for number, note in enumerate(pitch_names))