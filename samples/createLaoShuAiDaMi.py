# -*- coding: utf-8 -*-

import pretty_midi
from common import *

initial_tempo = 120.0
melody_c_melody = pretty_midi.PrettyMIDI(initial_tempo=initial_tempo)

###################################################### melody
melody_program = pretty_midi.instrument_name_to_program('Guitar harmonics')
melody = pretty_midi.Instrument(program = melody_program)

# 我听
add_instrument_note(instrument=melody, note_name='0', range=12)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)

# 见你的声音，有种
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=6)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)

# 特别的感觉，让
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=5)
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='A2', range=2)

# 我不断想，不
add_instrument_note(instrument=melody, note_name='G2', range=4)
add_instrument_note(instrument=melody, note_name='0', range=1)
add_instrument_note(instrument=melody, note_name='A2', range=1)
add_instrument_note(instrument=melody, note_name='A2', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=3)
add_instrument_note(instrument=melody, note_name='C3', range=1)

# 敢再忘记你，我记
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)

# 得有一个人，永远
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)

# 留在我心中，哪怕
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='B2', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=6)
add_instrument_note(instrument=melody, note_name='G2', range=1)
add_instrument_note(instrument=melody, note_name='G2', range=1)

# 只能够这样的想
add_instrument_note(instrument=melody, note_name='A2', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=3)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)

# 你，如果
add_instrument_note(instrument=melody, note_name='C3', range=8)
add_instrument_note(instrument=melody, note_name='0', range=4)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)

# 真的有一天，爱情
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=1)
add_instrument_note(instrument=melody, note_name='G3', range=3)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=4)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)

# 理想会实现，我会
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=3)
add_instrument_note(instrument=melody, note_name='E3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='G3', range=1)

# 加倍努力好好爱你
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=1)
add_instrument_note(instrument=melody, note_name='G3', range=3)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)

# 永远不改变，不管
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='A2', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='G3', range=1)

# 路有多么远，一定
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=1)
add_instrument_note(instrument=melody, note_name='G3', range=3)
add_instrument_note(instrument=melody, note_name='A3', range=4)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)

# 会让它实现，我会
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='G3', range=1)

# 轻轻在你耳边对你
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=4)

# 说，对你
add_instrument_note(instrument=melody, note_name='D3', range=6)
add_instrument_note(instrument=melody, note_name='0', range=4)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=3)

# 说，我爱
add_instrument_note(instrument=melody, note_name='E3', range=12)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)

# 你，爱着你，就像
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=5)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)

# 老鼠爱大米，不管
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='G3', range=1)

# 有多少风雨，我都会
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=1)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=3)
add_instrument_note(instrument=melody, note_name='G3', range=4)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=2)

# 一然陪着你，我想
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)

# 你，想着你，不管
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=5)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)

# 有多么的苦，只要
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=3)
add_instrument_note(instrument=melody, note_name='G3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='G3', range=1)

# 能让你开心，我什么都
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=3)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=3)
add_instrument_note(instrument=melody, note_name='G3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=2)

# 愿意，这样
add_instrument_note(instrument=melody, note_name='D3', range=8)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)

# 爱你
add_instrument_note(instrument=melody, note_name='D3', range=3)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=12)

notes = change_notes_tempo(melody.notes, 15.0/initial_tempo)
melody.notes = notes

melody_c_melody.instruments.append(melody)

melody_c_melody.write('LaoShuAiDaMi.midi')