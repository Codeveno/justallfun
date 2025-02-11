
# import the module
import winsound
import time

# define the frequency of the notes
freq = {'C': 523, 'D': 587, 'E': 659, 'F': 698, 'G': 784, 'A': 880, 'B': 988}

# define the duration of the notes
dur = 500

# define a function to play a note
def play(note, duration):
    winsound.Beep(freq[note], duration)
    time.sleep(duration / 1000)

# play the song
notes = [
    ('E', dur), ('E', dur), ('E', dur*2),
    ('E', dur), ('E', dur), ('E', dur*2),
    ('E', dur), ('G', dur), ('C', dur), ('D', dur), ('E', dur*2),
    ('F', dur), ('F', dur), ('F', dur), ('F', dur), ('F', dur), ('E', dur), ('E', dur), ('E', dur), ('E', dur), ('E', dur),
    ('E', dur), ('E', dur), ('E', dur), ('E', dur), ('E', dur), ('D', dur), ('D', dur), ('E', dur), ('D', dur*2), ('G', dur*2),
    ('E', dur), ('E', dur), ('E', dur*2),
    ('E', dur), ('E', dur), ('E', dur*2),
    ('E', dur), ('G', dur), ('C', dur), ('D', dur), ('E', dur*2),
    ('F', dur), ('F', dur), ('F', dur), ('F', dur), ('F', dur), ('E', dur), ('E', dur), ('E', dur), ('E', dur), ('E', dur),
    ('E', dur), ('E', dur), ('E', dur), ('E', dur), ('E', dur), ('D', dur), ('D', dur), ('E', dur), ('D', dur*2), ('G', dur*2)
]

for note, duration in notes:
    play(note, duration)
