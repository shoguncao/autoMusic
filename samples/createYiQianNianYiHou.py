# -*- coding: utf-8 -*-

import pretty_midi
from common import *

initial_tempo = 76.0
melody_c_melody = pretty_midi.PrettyMIDI(initial_tempo=initial_tempo)

###################################################### melody
melody_program = pretty_midi.instrument_name_to_program('Guitar harmonics')
melody = pretty_midi.Instrument(program = melody_program)

# 心跳乱了节奏
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C2', range=1)
add_instrument_note(instrument=melody, note_name='D2', range=1)
add_instrument_note(instrument=melody, note_name='E2', range=2)
add_instrument_note(instrument=melody, note_name='A2', range=2)
add_instrument_note(instrument=melody, note_name='G2', range=8)

# 梦也不自由
add_instrument_note(instrument=melody, note_name='F2', range=2)
add_instrument_note(instrument=melody, note_name='E2', range=1)
add_instrument_note(instrument=melody, note_name='C2', range=2)
add_instrument_note(instrument=melody, note_name='E2', range=2)
add_instrument_note(instrument=melody, note_name='D2', range=9)

# 爱是个绝对承诺不
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C2', range=1)
add_instrument_note(instrument=melody, note_name='D2', range=1)
add_instrument_note(instrument=melody, note_name='E2', range=2)
add_instrument_note(instrument=melody, note_name='A2', range=2)
add_instrument_note(instrument=melody, note_name='B2', range=3)
add_instrument_note(instrument=melody, note_name='G2', range=3)
add_instrument_note(instrument=melody, note_name='E2', range=2)

# 说，沉到一千年以后
add_instrument_note(instrument=melody, note_name='A2', range=8)
add_instrument_note(instrument=melody, note_name='B2', range=1)
add_instrument_note(instrument=melody, note_name='B2', range=1)
add_instrument_note(instrument=melody, note_name='B2', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='B2', range=2)

notes = change_notes_tempo(melody.notes, 15.0/initial_tempo)
melody.notes = notes

melody_c_melody.instruments.append(melody)

melody_c_melody.write('YiQianNianYiHou.midi')