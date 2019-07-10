#
#Creates a new Lilypond file
import random

file_name = "lilypond-test-" + (str(random.randrange(0, 100, 1)) + ".ly")
print(file_name)

def make_lilypond(file_name):
    new_file = open(file_name, "w+")
    new_file.write("test")
    new_file.close()
    return

make_lilypond(file_name)
