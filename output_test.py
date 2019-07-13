#
#Creates a new Lilypond file
import random

file_name = "lilypond-test-" + (str(random.randrange(0, 1000, 1)) + ".ly")
print(file_name)

#Template file contains basic info and formatting like version number,
#title, ect.
lp_template = open("lilypond_template.txt", "r")
template_text = lp_template.read()

#Should be self-explanatory
notes = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
guitar_range = ['e2', 'c6']
guitar_strings = ['e2', 'a2', 'd3', 'g3', 'b3', 'e4']

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

#make_lilypond(file_name, test_chord)
