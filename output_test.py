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
        suffix = has_accidental(pitch)
        note = pitch[0].lower()
        if isinstance(suffix, str):
            return note + suffix
        else:
            return note

def has_accidental(note):
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

def how_many_octaves(pitch_class):
    """how many particular instances of a specific pitch class are on each
    string? this function finds that out and stores it in a list, starting
    with the lowest string"""
    pitch = pitch_class
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
        print(str(l_string_position) + ' ' + str(h_string_position))
        note_position = notes.index(pitch[0])
        print(note_position)
        if not note_position >= l_string_position:
            current_octave += 1
        while current_octave < int(highest_note[(len(highest_note) - 1)]):
            if not current_octave in octaves:
                octaves.append(current_octave)
                current_octave += 1
                print(current_octave)
        if note_position <= h_string_position:
            octaves.append(current_octave)
        notes_on_each[lowest_note].append(octaves)
    return notes_on_each

print(how_many_octaves('e'))
#make_lilypond(file_name, test_chord)
