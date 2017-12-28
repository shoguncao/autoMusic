# -*- coding: utf-8 -*-

import pretty_midi
from common import *

initial_tempo = 240.0
melody_c_melody = pretty_midi.PrettyMIDI(initial_tempo=initial_tempo)

###################################################### melody
melody_program = pretty_midi.instrument_name_to_program('Guitar harmonics')
melody = pretty_midi.Instrument(program = melody_program)

# 对面的女孩
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='C3', range=4)

# 看过来
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 看过来
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='C4', range=8)

# 看过来
add_instrument_note(instrument=melody, note_name='B3', range=4)
add_instrument_note(instrument=melody, note_name='A3', range=4)
add_instrument_note(instrument=melody, note_name='G3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 这里的表演
add_instrument_note(instrument=melody, note_name='A3', range=4)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=4)
add_instrument_note(instrument=melody, note_name='F3', range=4)

# 很精彩
add_instrument_note(instrument=melody, note_name='G3', range=4)
add_instrument_note(instrument=melody, note_name='G3', range=4)
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 请不要假装
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='D3', range=4)

# 不理不睬
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=4)
add_instrument_note(instrument=melody, note_name='G3', range=12)
add_instrument_note(instrument=melody, note_name='0', range=12)

# 对面的女孩
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='C3', range=4)

# 看过来
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 看过来
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='C4', range=8)

# 看过来
add_instrument_note(instrument=melody, note_name='B3', range=4)
add_instrument_note(instrument=melody, note_name='A3', range=4)
add_instrument_note(instrument=melody, note_name='G3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 不要被我的
add_instrument_note(instrument=melody, note_name='A3', range=4)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=4)
add_instrument_note(instrument=melody, note_name='F3', range=4)

# 样子吓坏
add_instrument_note(instrument=melody, note_name='G3', range=4)
add_instrument_note(instrument=melody, note_name='G3', range=4)
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 其实我
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 很可爱
add_instrument_note(instrument=melody, note_name='G3', range=4)
add_instrument_note(instrument=melody, note_name='E3', range=4)
add_instrument_note(instrument=melody, note_name='G3', range=12)
add_instrument_note(instrument=melody, note_name='0', range=12)

# 寂寞男孩
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='C3', range=4)

# 的悲哀
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 说出来
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='C4', range=8)

# 谁明白
add_instrument_note(instrument=melody, note_name='B3', range=4)
add_instrument_note(instrument=melody, note_name='A3', range=4)
add_instrument_note(instrument=melody, note_name='G3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 求求你抛个
add_instrument_note(instrument=melody, note_name='A3', range=4)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=4)
add_instrument_note(instrument=melody, note_name='F3', range=4)

# 媚眼过来
add_instrument_note(instrument=melody, note_name='G3', range=4)
add_instrument_note(instrument=melody, note_name='G3', range=4)
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 哄哄我逗我
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)

# 乐开怀
add_instrument_note(instrument=melody, note_name='G3', range=4)
add_instrument_note(instrument=melody, note_name='G3', range=4)
add_instrument_note(instrument=melody, note_name='G3', range=12)
add_instrument_note(instrument=melody, note_name='0', range=12)

# 我左看
add_instrument_note(instrument=melody, note_name='0', range=6)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=4)
add_instrument_note(instrument=melody, note_name='G4', range=4)

# 右看上看
add_instrument_note(instrument=melody, note_name='G4', range=4)
add_instrument_note(instrument=melody, note_name='B3', range=4)
add_instrument_note(instrument=melody, note_name='B3', range=4)
add_instrument_note(instrument=melody, note_name='D4', range=4)

# 下看，原来每个
add_instrument_note(instrument=melody, note_name='D4', range=4)
add_instrument_note(instrument=melody, note_name='C4', range=4)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)

# 女孩都不简单
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=4)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=6)

# 我想了又
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=4)
add_instrument_note(instrument=melody, note_name='G4', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=4)

# 想我猜了又
add_instrument_note(instrument=melody, note_name='B3', range=4)
add_instrument_note(instrument=melody, note_name='B3', range=2)
add_instrument_note(instrument=melody, note_name='B3', range=4)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=4)

# 猜，女孩们的
add_instrument_note(instrument=melody, note_name='C4', range=6)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)

# 心思还真奇怪
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=4)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=14)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 寂寞男孩
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='C3', range=4)

# 苍蝇拍
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 左拍拍
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='C4', range=8)

# 右拍拍
add_instrument_note(instrument=melody, note_name='B3', range=4)
add_instrument_note(instrument=melody, note_name='A3', range=4)
add_instrument_note(instrument=melody, note_name='G3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 为什么还是
add_instrument_note(instrument=melody, note_name='A3', range=4)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=4)
add_instrument_note(instrument=melody, note_name='F3', range=4)

# 没人来爱
add_instrument_note(instrument=melody, note_name='G3', range=4)
add_instrument_note(instrument=melody, note_name='G3', range=4)
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 无人问津哪
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 真无奈
add_instrument_note(instrument=melody, note_name='G3', range=4)
add_instrument_note(instrument=melody, note_name='E3', range=4)
add_instrument_note(instrument=melody, note_name='G3', range=12)
add_instrument_note(instrument=melody, note_name='0', range=12)

# 对面的女孩
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='C3', range=4)

# 看过来
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 看过来
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='C4', range=8)

# 看过来
add_instrument_note(instrument=melody, note_name='B3', range=4)
add_instrument_note(instrument=melody, note_name='A3', range=4)
add_instrument_note(instrument=melody, note_name='G3', range=8)

# 寂寞男孩
add_instrument_note(instrument=melody, note_name='A3', range=4)
add_instrument_note(instrument=melody, note_name='A3', range=4)
add_instrument_note(instrument=melody, note_name='G3', range=4)
add_instrument_note(instrument=melody, note_name='F3', range=4)

# 情窦初开
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=4)
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 需要你给我
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)

# 一点爱
add_instrument_note(instrument=melody, note_name='G3', range=4)
add_instrument_note(instrument=melody, note_name='E3', range=4)
add_instrument_note(instrument=melody, note_name='G3', range=12)
add_instrument_note(instrument=melody, note_name='0', range=12)

# 嘿
add_instrument_note(instrument=melody, note_name='B3', range=12)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 嘿，我
add_instrument_note(instrument=melody, note_name='D4', range=12)
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)

# 左看右看
add_instrument_note(instrument=melody, note_name='C4', range=4)
add_instrument_note(instrument=melody, note_name='G4', range=4)
add_instrument_note(instrument=melody, note_name='G4', range=4)
add_instrument_note(instrument=melody, note_name='B3', range=4)

# 上看下看
add_instrument_note(instrument=melody, note_name='B3', range=4)
add_instrument_note(instrument=melody, note_name='D4', range=4)
add_instrument_note(instrument=melody, note_name='D4', range=4)
add_instrument_note(instrument=melody, note_name='C4', range=4)

# 原来每个女孩都
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)

# 不简单，我
add_instrument_note(instrument=melody, note_name='E4', range=4)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=6)
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)

# 想了又想，我
add_instrument_note(instrument=melody, note_name='C4', range=4)
add_instrument_note(instrument=melody, note_name='G4', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=4)
add_instrument_note(instrument=melody, note_name='B3', range=4)
add_instrument_note(instrument=melody, note_name='B3', range=2)

# 猜了又才
add_instrument_note(instrument=melody, note_name='B3', range=4)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=4)
add_instrument_note(instrument=melody, note_name='C4', range=6)

# 女孩们的心事还
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)

# 真奇怪，我
add_instrument_note(instrument=melody, note_name='E4', range=4)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=6)
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)

# 左看右看
add_instrument_note(instrument=melody, note_name='C4', range=4)
add_instrument_note(instrument=melody, note_name='G4', range=4)
add_instrument_note(instrument=melody, note_name='G4', range=4)
add_instrument_note(instrument=melody, note_name='B3', range=4)

# 上看下看
add_instrument_note(instrument=melody, note_name='B3', range=4)
add_instrument_note(instrument=melody, note_name='D4', range=4)
add_instrument_note(instrument=melody, note_name='D4', range=4)
add_instrument_note(instrument=melody, note_name='C4', range=4)

# 原来每个女孩都
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)

# 不简单，我
add_instrument_note(instrument=melody, note_name='E4', range=4)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=6)
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)

# 想了又想，我
add_instrument_note(instrument=melody, note_name='C4', range=4)
add_instrument_note(instrument=melody, note_name='G4', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=4)
add_instrument_note(instrument=melody, note_name='B3', range=4)
add_instrument_note(instrument=melody, note_name='B3', range=2)

# 猜了又才
add_instrument_note(instrument=melody, note_name='B3', range=4)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=4)
add_instrument_note(instrument=melody, note_name='C4', range=6)

# 女孩们的心事还
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)

# 真奇怪，哎，真奇
add_instrument_note(instrument=melody, note_name='E4', range=4)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=14)
add_instrument_note(instrument=melody, note_name='G4', range=4)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='0', range=2)

# 怪，唻唻唻~~
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=3)
add_instrument_note(instrument=melody, note_name='B3', range=4)

# 唻
add_instrument_note(instrument=melody, note_name='B3', range=1)
add_instrument_note(instrument=melody, note_name='B3', range=3)
add_instrument_note(instrument=melody, note_name='C4', range=4)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 唻
add_instrument_note(instrument=melody, note_name='C4', range=3)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=4)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='0', range=2)

# 哦嘿哦
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=6)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 唻
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='B3', range=4)

# 唻
add_instrument_note(instrument=melody, note_name='B3', range=1)
add_instrument_note(instrument=melody, note_name='B3', range=3)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='0', range=2)

# 唻
add_instrument_note(instrument=melody, note_name='C4', range=3)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=4)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)

# 奥
add_instrument_note(instrument=melody, note_name='D4', range=24)
add_instrument_note(instrument=melody, note_name='0', range=8)

notes = change_notes_tempo(melody.notes, 15.0/initial_tempo)
melody.notes = notes

melody_c_melody.instruments.append(melody)

melody_c_melody.write('DuiMianDeNvHaiKanGuoLai.midi')