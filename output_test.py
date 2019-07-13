#
#Creates a new Lilypond file
import random

file_name = "lilypond-test-" + (str(random.randrange(0, 100, 1)) + ".ly")
print(file_name)

notes = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
lp_template = open("lilypond_template.txt", "r")
template_text = lp_template.read()

test_chord = ['a', 'cis', 'e']

def make_lilypond(file_name, notes):
    global template_text
    new_file = open(file_name, "w+")
    new_file.write(template_text)
    new_file.write("{\n")
    for note in notes:
        if notes.index(note) == 0:
            new_file.write(note + '4 ')
        else:
            new_file.write(note + ' ')
    new_file.write('\n}')
    new_file.close()
    return

def has_accidental(note):
    pitch_class = list(note)
    if pitch_class.len() >= 2:
        for character in pitch:
            if character == '#':
                return 'is'
            elif character == 'b':
                return 'es'
            else:
                return

def what_is_note(pitch):
    if isinstance(pitch, str):
        suffix = has_accidental(pitch)
        note = pitch[0]
        return note + suffix

make_lilypond(file_name, test_chord)
