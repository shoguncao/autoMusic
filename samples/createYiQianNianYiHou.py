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

# 放任无奈，淹没尘埃
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='B2', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=3)
add_instrument_note(instrument=melody, note_name='B2', range=2)
add_instrument_note(instrument=melody, note_name='A2', range=1)
add_instrument_note(instrument=melody, note_name='B2', range=2)
add_instrument_note(instrument=melody, note_name='G2', range=3)

# 我在废墟之中守着你走来，哦
add_instrument_note(instrument=melody, note_name='A2', range=1)
add_instrument_note(instrument=melody, note_name='A2', range=1)
add_instrument_note(instrument=melody, note_name='B2', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='F3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)

# 我的泪光承载不了哦
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='B2', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=3)
add_instrument_note(instrument=melody, note_name='B2', range=2)
add_instrument_note(instrument=melody, note_name='A2', range=1)
add_instrument_note(instrument=melody, note_name='B2', range=3)
add_instrument_note(instrument=melody, note_name='G2', range=1)
add_instrument_note(instrument=melody, note_name='A2', range=2)

# 所有一切你要的
add_instrument_note(instrument=melody, note_name='C3', range=7)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=3)

# 爱，因为在
add_instrument_note(instrument=melody, note_name='D3', range=6)
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='B2', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=3)

# 一千年以后，世界
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='G2', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=5)
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)

# 早已没有我，无法
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='B2', range=1)
add_instrument_note(instrument=melody, note_name='A2', range=2)
add_instrument_note(instrument=melody, note_name='E2', range=2)
add_instrument_note(instrument=melody, note_name='B2', range=5)
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='B2', range=1)

# 深情挽着你的手，亲
add_instrument_note(instrument=melody, note_name='A2', range=2)
add_instrument_note(instrument=melody, note_name='B2', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='G2', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=4)
add_instrument_note(instrument=melody, note_name='E3', range=1)

# 吻着你额头，别等到
add_instrument_note(instrument=melody, note_name='F3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='B2', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=3)

# 一千年以后，所有人
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='G2', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=5)
add_instrument_note(instrument=melody, note_name='0', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)

notes = change_notes_tempo(melody.notes, 15.0/initial_tempo)
melody.notes = notes

melody_c_melody.instruments.append(melody)

melody_c_melody.write('YiQianNianYiHou.midi')