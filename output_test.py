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
    ['b3','g5'],
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

#make_lilypond(file_name, test_chord)

#making new classes right here

class Pitch_Class(object):
    def __init__(self, pitch):
        self.pitch = pitch
        self.octaves = None
    def set_octaves(self):
        """how many particular instances of a specific pitch class are on each
        string? this function finds that out and stores it in a list, starting
        on the lowest string
        """
        notes_on_each = []
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
                if not len(pitch) == 1:
                    if not note_position == h_string_position or not pitch[1] == "#":
                        octaves.append(current_octave)
                else:
                    octaves.append(current_octave)
            notes_on_each.append(octaves)
            current_string += 1
        self.octaves = notes_on_each
        return
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
    def set_fret(self):
        """figures out which fret a given note is played using on a particular
        string"""
        global guitar_strings
        pitch_class = str(self.pitch[0])
        octave = int(self.octave)
        current_string = guitar_strings[self.string]
        string_pitch = current_string[0][0]
        string_octave = int(current_string[0][-1])
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
        if fret <= 22 and fret >= 0:
            self.fret = fret
        return
    def get_fret(self):
        return self.fret
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

class Pitch_Collection(object):
    #A collection of pitch classes without defined octaves/strings, used as the
    #basis for more definite chords
    def __init__(self, pitches):
        self.pitches = pitches
        return

class Chord(Pitch_Collection):
    #A chord that contains at least 2 definite pitches including their octave,
    #string, and fret
    def __init__(self, pitches):
        Collection.__init__(self, pitches)
        self.notes = []
        return
    def __str__(self):
        pitch_classes = []
        for note in self.notes:
            pitch_classes.append(note.pitch)
        return "the notes in this chord are " + str(pitch_classes)
    def get_notes(self):
        return self.notes
    def print_lilypond(self):
        return

def make_a_bunch_of_chords(pitch_collection):
    chord_pitches = []
    all_the_pc = []
    current_chord = []
    all_the_notes = []
    possible_roots = []
    string = 0
    for note in pitch_collection:
        chord_pitches.append(note)
    for pitch in chord_pitches:
        #this is where we start with the root and iterate through different voicings
        #based on the each one
        current_root = Pitch_Class(pitch)
        current_root.set_octaves()
        root_octaves = current_root.get_octaves()
        #creates a list of all possible notes to be used based on the given pitch collection
        while string <= (len(guitar_strings)-1):
            octave_to_add = root_octaves[string][0]
            while octave_to_add in root_octaves[string]:
                if not (pitch+str(octave_to_add)) in all_the_pc:
                    #print(octave_to_add)
                    all_the_pc.append(pitch+str(octave_to_add))
                    octave_to_add += 1
                    print(all_the_pc)
                else:
                    octave_to_add += 1
            string += 1
            continue
        string = 0
    for pc in all_the_pc:
        string = 0
        while string <= (len(guitar_strings)-1):
            #finding the fret position of each note
            if len(pc) == 2:
                root = Note(pc[0], pc[1])
            else:
                root = Note(pc[0]+pc[1], pc[2])
            root.set_string(string)
            root.set_fret()
            if root.get_fret() != None:
                print(root.get_string())
                print(root.get_fret())
                #for some reason notes too low in range to be on string
                #are still being added, need to figure out why
                possible_roots.append(root)
            string += 1
    for i in range(len(possible_roots)):
        for j in range(i + 1, len(possible_roots)):
            current_chord.append(possible_roots[i])
            if -3 <= possible_roots[i].get_fret() - possible_roots[j].get_fret() <= 3:
                if possible_roots[i].get_string()
                    current_chord.append(possible_roots[j])
    return

test_collection = Pitch_Collection(test_chord_notes)
make_a_bunch_of_chords(test_collection.pitches)
