#
#Creates a new Lilypond file
import random
from collections import defaultdict

file_name = "lilypond-test-" + (str(random.randrange(0, 1000, 1)) + ".ly")
print(file_name)

#Template file contains basic info and formatting like version number,
#title, ect.
lp_template = open("templates/lilypond_template.txt", "r")
template_text = lp_template.read()

#Should be self-explanatory, in this order b/c octaves start with C for some
#reason even though we start the alphabet over at g????
notes = ['c', 'd', 'e', 'f', 'g', 'a', 'b']
guitar_strings = {
    'e2':'c4',
    'a2':'f4',
    'd3':'bb4',
    'g3':'eb5',
    'b3':'g6',
    'e4':'c6'
}
#for test purposes only, will be replaced with data submitted by user
test_chord = ['a', 'c#', 'e']

def make_lilypond(notes):
    """writes the given notes to a new lilypond file with a random name"""
    global file_name
    global template_text
    new_file = open(file_name, "w+")
    new_file.write(template_text)
    new_file.write("{\n")
    new_file.write('\clef "treble_8"\n')
    for note in notes:
        note_string = what_is_note(note)
        if notes.index(note) == 0:
            new_file.write(note_string + '4 ')
        else:
            new_file.write(note_string + ' ')
    new_file.write('\n}')
    new_file.close()
    return

def what_is_note(pitch):
    """transforms the given input into data that will result in the
    desired notes in lilypond by attaching the appropriate suffix for sharp
    or flat notes"""
    if isinstance(pitch, str):
        suffix = translate_accidental(pitch)
        note = pitch[0].lower()
        if isinstance(suffix, str):
            return note + suffix
        else:
            return note

def translate_accidental(note):
    """if the given pitch has an accidental, the function will return the
    appropriate lilypond suffix"""
    pitch_class = list(note)
    if len(pitch_class) >= 2:
            if pitch_class[1] == '#':
                return 'is'
            elif pitch_class[1] == 'b':
                return 'es'
            else:
                return

def find_chords(notes):
    return

#make_lilypond(file_name, test_chord)

#making new classes right here
class Pitch_Class(object):
    def __init__(self, pitch):
        self.pitch = pitch
        self.octaves = None
    def set_pitch(self, newpitch):
        self.pitch = newpitch
    def set_octaves(self):
        """how many particular instances of a specific pitch class are on each
        string? this function finds that out and stores it in a list, starting
        on the lowest string
        """
        notes_on_each = defaultdict(list)
        global guitar_strings
        global notes
        for lowest_note in guitar_strings:
            current_string = lowest_note
            highest_note = guitar_strings[lowest_note]
            octaves = []
            current_octave = int(lowest_note[1])
            l_string_position = notes.index(lowest_note[0])
            h_string_position = notes.index(highest_note[0])
            note_position = notes.index(self.pitch[0])
            if not note_position >= l_string_position:
                current_octave += 1
            while current_octave < int(highest_note[(len(highest_note) - 1)]):
                if not current_octave in octaves:
                    octaves.append(current_octave)
                    current_octave += 1
            if note_position <= h_string_position:
                octaves.append(current_octave)
            notes_on_each[lowest_note].append(octaves)
        self.octaves = notes_on_each
    def get_pitch(self):
        return self.pitch
    def get_octaves(self):
        return self.octaves
    def __str__(self):
        return "pitch_class: "+str(self.pitch)+str(self.octaves)

class Note(Pitch_Class):
    def __init__(self, pitch):
        Pitch_Class.__init__(self, pitch)
        self.octave = None
        self.string = None
        self.fret = None
    def set_fret(self):
        """figures out which fret a given note is played using on a particular
        string"""
        pitch_class = str(self.pitch[0])
        octave = int(self.pitch[-1])
        string_pitch = str(self.string[0])
        string_octave = int(self.string[-1])
        fret = 0
        if notes.index(pitch_class) > notes.index(string_pitch):
            if notes.index(pitch_class) >= 3:
                fret += (2 * (notes.index(pitch_class) - notes.index(string_pitch)) - 1)
                #accounts for half step in between E and F, distance of only 1 fret
                #instead of 2
            else:
                fret += 2 * (notes.index(pitch_class) - notes.index(string_pitch))
        elif notes.index(pitch_class) < notes.index(string_pitch):
            if notes.index(pitch_class) <= 2:
                fret -= (2 * (notes.index(string_pitch) - notes.index(pitch_class)) + 1)
                #adds back the half step present between E and F, sim to above
            else:
                fret -= 2 * (notes.index(pitch_class) - notes.index(string_pitch))
        while octave > string_octave:
            fret += 12
            string_octave += 1
        self.fret = fret
        return
    def __str__(self):
        return "note: "+str(self.octave)+str(self.string)+str(self.fret)

class Chord(object):
    def __init__(self, notes):
        self.notes = notes
    def get_notes(self):
        return self.notes
    def print_lilypond(self):
        return

note_1 = Pitch_Class(test_chord[0])
note_1.set_octaves()
note_2 = []
note_3 = []
note_4 = []

print(note_1.get_pitch())
print(note_1.get_octaves())
