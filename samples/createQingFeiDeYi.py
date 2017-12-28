# -*- coding: utf-8 -*-

import pretty_midi
from common import *

initial_tempo = 120.0
melody_c_melody = pretty_midi.PrettyMIDI(initial_tempo=initial_tempo)

###################################################### melody
melody_program = pretty_midi.instrument_name_to_program('Guitar harmonics')
melody = pretty_midi.Instrument(program = melody_program)

# 难以
add_instrument_note(instrument=melody, note_name='0', range=12)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=2)

# 忘记初次见你
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=4)
add_instrument_note(instrument=melody, note_name='G3', range=4)
add_instrument_note(instrument=melody, note_name='F3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=6)

# 一双
add_instrument_note(instrument=melody, note_name='0', range=8)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)

# 迷人的眼睛
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='C4', range=6)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=6)

# 在我
add_instrument_note(instrument=melody, note_name='0', range=8)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)

# 脑海里你
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=6)
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)

# 的身影
add_instrument_note(instrument=melody, note_name='B3', range=4)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='B3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 挥散不去
add_instrument_note(instrument=melody, note_name='C3', range=6)
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='D3', range=6)

# 握你的
add_instrument_note(instrument=melody, note_name='0', range=6)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=2)

# 双手感觉你的温柔
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=10)

# 真的
add_instrument_note(instrument=melody, note_name='0', range=4)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)

# 有点透不过气
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='C4', range=4)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=10)

# 你
add_instrument_note(instrument=melody, note_name='0', range=6)
add_instrument_note(instrument=melody, note_name='G3', range=2)

# 的天真我
add_instrument_note(instrument=melody, note_name='A3', range=4)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=6)
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=2)

# 想珍惜，看到
add_instrument_note(instrument=melody, note_name='B3', range=4)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=6)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)

# 你受委屈我会伤心
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=10)

# 哦
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=3)

# 只怕我
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=1)
add_instrument_note(instrument=melody, note_name='B3', range=1)
add_instrument_note(instrument=melody, note_name='A3', range=1)
add_instrument_note(instrument=melody, note_name='G3', range=3)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=2)

# 自己会爱上你
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=4)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=4)
add_instrument_note(instrument=melody, note_name='G4', range=10)

# 不敢
add_instrument_note(instrument=melody, note_name='0', range=4)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=2)

# 让自己靠的太近
add_instrument_note(instrument=melody, note_name='G4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=4)
add_instrument_note(instrument=melody, note_name='F4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=10)

# 怕我
add_instrument_note(instrument=melody, note_name='0', range=4)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=2)

# 没什么能够给你
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=4)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=10)

# 爱你
add_instrument_note(instrument=melody, note_name='0', range=4)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)

# 也需要很大的勇气
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=10)

# 只怕我
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=2)

# 自己会爱上你
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=4)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=4)
add_instrument_note(instrument=melody, note_name='G4', range=10)

# 也许
add_instrument_note(instrument=melody, note_name='0', range=4)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=2)

# 有天会情不自禁
add_instrument_note(instrument=melody, note_name='G4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=4)
add_instrument_note(instrument=melody, note_name='F4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=10)

# 想念
add_instrument_note(instrument=melody, note_name='0', range=4)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=2)

# 只让自己苦了自己
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=10)

# 爱上
add_instrument_note(instrument=melody, note_name='0', range=4)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)

# 你是我情非得已
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=4)
add_instrument_note(instrument=melody, note_name='C4', range=10)
add_instrument_note(instrument=melody, note_name='0', range=8)

notes = change_notes_tempo(melody.notes, 15.0/initial_tempo)
melody.notes = notes

melody_c_melody.instruments.append(melody)

melody_c_melody.write('QingFeiDeYi.midi')