'''
Print guitar scales to stdout
'''
import argparse
import textwrap

MAXFRET = 16
NOTES_FLAT = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
NOTES_SHARP = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

# Scale dictionary
SCALEDICT = [
    ['Scale', 'Chromatic', '1,b2,2,b3,3,4,b5,5,b6,6,b7,7'],
    ['Scale', 'Major', '1,2,3,4,5,6,7'],
    ['Scale', 'Minor Natural', '1,2,b3,4,5,b6,b7'],
    ['Scale', 'Minor Harmonic', '1,2,b3,4,5,b6,7'],
    ['Scale', 'Major Pentatonic', '1,2,3,5,6'],
    ['Scale', 'Minor Pentatonic', '1,b3,4,5,b7'],
    ['Scale', 'Blues Pentatonic', '1,b3,4,b5,5,b7'],
    ['Mode', 'Ionian', '1,2,3,4,5,6,7'],
    ['Mode', 'Dorian', '1,2,b3,4,5,6,b7'],
    ['Mode', 'Phrygian', '1,b2,b3,4,5,b6,b7'],
    ['Mode', 'Lydian', '1,2,3,#4,5,6,7'],
    ['Mode', 'Mixolydian', '1,2,3,4,5,6,b7'],
    ['Mode', 'Aeolian', '1,2,b3,4,5,b6,b7'],
    ['Mode', 'Locrian', '1,b2,b3,4,b5,b6,b7'],
    ['Chord', 'Major', '1,3,5'],
    ['Chord', 'Minor', '1,b3,5'],
    ['Chord', '7th', '1,3,5,b7'],
    ['Chord', 'Major 7th', '1,3,5,7'],
    ['Chord', 'Minor 7th', '1,b3,5,b7'],
    ['Chord', '6th', '1,3,5,6'],
    ['Chord', 'Augmented', '1,3,#5'],
    ['Chord', 'Diminished', '1,b3,b5']
]
