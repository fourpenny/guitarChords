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
guitar_strings = [
    ['e2','c4'],
    ['a2','f4'],
    ['d3','bb4'],
    ['g3','eb5'],
    ['b3','g6'],
    ['e4','c6']
]
#for test purposes only, will be replaced with data submitted by user
test_chord_notes = ['a', 'c#', 'e']

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
class Guitar_String(object):
    def __init__(self, lowest_note, highest_note):
        self.lowest_note = lowest_note
        self.highest_note = highest_note

class Pitch_Class(object):
    def __init__(self, pitch):
        self.pitch = pitch
        self.octaves = None
    def set_octaves(self):
        """how many particular instances of a specific pitch class are on each
        string? this function finds that out and stores it in a list, starting
        on the lowest string
        """
        notes_on_each = defaultdict(list)
        global guitar_strings
        global notes
        current_string = 0
        while current_string < 6:
            lowest_note = guitar_strings[current_string][0]
            pitch = str(self.pitch)
            highest_note = guitar_strings[current_string][1]
            octaves = []
            current_octave = int(lowest_note[1])
            l_string_position = notes.index(lowest_note[0])
            h_string_position = notes.index(highest_note[0])
            note_position = notes.index(pitch[0])
            #is the note above or below the fundamental of the given string?
            if not note_position >= l_string_position:
                current_octave += 1
            while current_octave < int(highest_note[(len(highest_note) - 1)]):
                if not current_octave in octaves:
                    octaves.append(current_octave)
                    current_octave += 1
            if note_position <= h_string_position:
                octaves.append(current_octave)
            notes_on_each[lowest_note].append(octaves)
            current_string += 1
        self.octaves = notes_on_each

    def get_pitch(self):
        return self.pitch
    def get_octaves(self):
        return self.octaves
    def __str__(self):
        return "pitch_class: "+str(self.pitch)+" "+str(self.octaves)

class Note(Pitch_Class):
    def __init__(self, pitch, octave):
        Pitch_Class.__init__(self, pitch)
        self.octave = octave
        self.string = None
        self.fret = None
    def set_fret(self, string):
        """figures out which fret a given note is played using on a particular
        string"""
        global guitar_strings
        pitch_class = str(self.pitch[0])
        octave = int(self.octave)
        current_string = guitar_strings[0]
        string_pitch = current_string[0][0]
        string_octave = int(current_string[0][-1])
        fret = 0
        print(pitch_class)
        print(current_string)
        print(string_pitch)
        print(string_octave)
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
    def set_octave(self, octave):
        self.octave = octave
        return
    def get_octave(self):
        return self.octave
    def set_string(self,string):
        self.string = string
        return
    def get_string(self):
        return self.string
    def __str__(self):
        return "note: "+str(self.pitch)+str(self.octave)+" "+str(self.string)+" "+str(self.fret)

class Chord(object):
    def __init__(self, notes):
        self.notes = notes
    def __str__(self):
        pitch_classes = []
        for note in self.notes:
            pitch_classes.append(note.pitch)
        return "the notes in this chord are " + str(pitch_classes)
    def __getitem__(self,index):
        return self.notes[index]
    def set_root(self):
        self.root = self.notes[0]
        return
    def what_string_is_root_on(self):
        """is the root note in the given octave on a given string???"""
        return
    def get_root(self):
        return self.root
    def get_notes(self):
        return self.notes
    def print_lilypond(self):
        return

note_1 = Pitch_Class(test_chord_notes[0])
note_1.set_octaves()
note_2 = Pitch_Class(test_chord_notes[1])
note_2.set_octaves()
note_3 = Pitch_Class(test_chord_notes[2])
note_3.set_octaves()

def make_a_bunch_of_chords(all_the_notes):
    chord_pitches = []
    for note in all_the_notes:
        chord_pitches.append(str(note.pitch))
    print(chord_pitches)
    for pitch in chord_pitches:
        string = 0
        current_pitch = Pitch_Class(pitch)
        current_pitch.set_octaves()
        pitch_octaves = current_pitch.get_octaves()
        print(pitch_octaves)
        current_note_ocatves = list(pitch_octaves.copy().values())
        for octaves in current_note_ocatves:
            if string < 5:
                root_pc = str(current_pitch.get_pitch())
                root_octave = current_note_ocatves[0][0][0]
                root_note = Note(root_pc, root_octave)
                root_note.set_string(string)
                root_note.set_fret(string)
                print(root_note)
                break
            #if pitch in root_notes:
                #if not second_note in chord:
                    #if not third_note in chord:
                        #ect... do a loop (duh)
                    #if not number_of_chords with this root > 10:
                    #make a chord based off of given data
                    #else:
                        #root note isn't on the string and the string isn't the highest one
                        #string += 1
                        #done with this root note, go to the next one

    return


test_chord = Chord([note_1, note_2, note_3])
make_a_bunch_of_chords(test_chord.notes)
