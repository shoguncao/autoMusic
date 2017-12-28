# -*- coding: utf-8 -*-

import pretty_midi
from common import *

initial_tempo = 76.0
melody_c_melody = pretty_midi.PrettyMIDI(initial_tempo=initial_tempo)

###################################################### melody
melody_program = pretty_midi.instrument_name_to_program('Guitar harmonics')
melody = pretty_midi.Instrument(program = melody_program)

# 前奏balabala
add_instrument_note(instrument=melody, note_name='G2', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='A2', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='G2', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='A2', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=5)

add_instrument_note(instrument=melody, note_name='G2', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='A2', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='G2', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='A2', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='B2', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)

add_instrument_note(instrument=melody, note_name='G2', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='A2', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='G2', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='A2', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='G2', range=4)

add_instrument_note(instrument=melody, note_name='G2', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='A2', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='G2', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='A2', range=3)
add_instrument_note(instrument=melody, note_name='B2', range=4)

# 一盏离愁孤单
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=4)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)

# 伫立在窗口
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='A2', range=2)
add_instrument_note(instrument=melody, note_name='A2', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 我在门后假装
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=4)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)

# 你人还没走
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='A2', range=2)
add_instrument_note(instrument=melody, note_name='A2', range=2)
add_instrument_note(instrument=melody, note_name='G2', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 旧地如重游月圆
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=2)

# 更寂寞
add_instrument_note(instrument=melody, note_name='G3', range=4)
add_instrument_note(instrument=melody, note_name='F3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=6)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 夜半清醒的烛火
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='A2', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)

# 不忍苛责我
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=8)

# 一壶漂泊浪迹
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=4)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)

# 天涯难入喉
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='A2', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 你走之后酒暖
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=4)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)

# 回忆思念瘦
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=8)

# 水向东流时间
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=4)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=2)

# 怎么偷
add_instrument_note(instrument=melody, note_name='G3', range=4)
add_instrument_note(instrument=melody, note_name='F3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=6)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 花开就一次成熟
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='A2', range=2)

# 我却错过
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=10)

# 间奏balabala
add_instrument_note(instrument=melody, note_name='A3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='G3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='A2', range=1)
add_instrument_note(instrument=melody, note_name='G2', range=1)
add_instrument_note(instrument=melody, note_name='A2', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='G3', range=1)
add_instrument_note(instrument=melody, note_name='A3', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=1)

# 谁在用琵琶弹奏
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=3)
add_instrument_note(instrument=melody, note_name='B3', range=1)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)

# 一曲东风破
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 岁月在墙上剥落
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)

# 看见小时候
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 犹记得那年我们
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)

# 都还很年幼
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='A2', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 而如今琴声幽幽
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)

# 我的等候你没听过
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)

# 谁在用琵琶弹奏
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=3)
add_instrument_note(instrument=melody, note_name='B3', range=1)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)

# 一曲东风破
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 枫叶将故事染色
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)

# 结局我看透
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 篱笆外的古道我
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)

# 牵着你走过
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 荒烟蔓草的年头
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=3)
add_instrument_note(instrument=melody, note_name='G3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)

# 就连分手都很沉
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='A2', range=2)

# 默
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=8)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='A2', range=4)

# 间奏balabala
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='G3', range=8)

add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=8)
add_instrument_note(instrument=melody, note_name='A3', range=1)
add_instrument_note(instrument=melody, note_name='G3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=3)
add_instrument_note(instrument=melody, note_name='D3', range=1)

add_instrument_note(instrument=melody, note_name='E3', range=3)
add_instrument_note(instrument=melody, note_name='G3', range=3)
add_instrument_note(instrument=melody, note_name='E3', range=10)

add_instrument_note(instrument=melody, note_name='A3', range=10)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=3)
add_instrument_note(instrument=melody, note_name='E3', range=1)

add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='A2', range=11)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)

add_instrument_note(instrument=melody, note_name='D3', range=10)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='A2', range=1)
add_instrument_note(instrument=melody, note_name='G2', range=2)
add_instrument_note(instrument=melody, note_name='A2', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=3)

add_instrument_note(instrument=melody, note_name='C3', range=14)

# 一壶漂泊浪迹
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=4)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)

# 天涯难入喉
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='A2', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 你走之后酒暖
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=4)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)

# 回忆思念瘦
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=8)

# 水向东流时间
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=4)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=2)

# 怎么偷
add_instrument_note(instrument=melody, note_name='G3', range=4)
add_instrument_note(instrument=melody, note_name='F3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=6)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 花开就一次成熟
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='A2', range=2)

# 我却错过
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=10)

# 间奏balabala
add_instrument_note(instrument=melody, note_name='A3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='G3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='A2', range=1)
add_instrument_note(instrument=melody, note_name='G2', range=1)
add_instrument_note(instrument=melody, note_name='A2', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='G3', range=1)
add_instrument_note(instrument=melody, note_name='A3', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=1)

# 谁在用琵琶弹奏
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=3)
add_instrument_note(instrument=melody, note_name='B3', range=1)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)

# 一曲东风破
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 岁月在墙上剥落
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)

# 看见小时候
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 犹记得那年我们
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)

# 都还很年幼
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='A2', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 而如今琴声幽幽
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)

# 我的等候你没听过
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)

# 谁在用琵琶弹奏
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=3)
add_instrument_note(instrument=melody, note_name='B3', range=1)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)

# 一曲东风破
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 枫叶将故事染色
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)

# 结局我看透
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 篱笆外的古道我
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)

# 牵着你走过
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 荒烟蔓草的年头
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=3)
add_instrument_note(instrument=melody, note_name='G3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)

# 就连分手都
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 谁在用琵琶弹奏
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=3)
add_instrument_note(instrument=melody, note_name='B3', range=1)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)

# 一曲东风破
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 岁月在墙上剥落
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)

# 看见小时候
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 犹记得那年我们
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)

# 都还很年幼
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='A2', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 而如今琴声幽幽
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)

# 我的等候你没听过
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)

# 谁在用琵琶弹奏
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=3)
add_instrument_note(instrument=melody, note_name='B3', range=1)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)

# 一曲东风破
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 枫叶将故事染色
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)

# 结局我看透
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 篱笆外的古道我
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)

# 牵着你走过
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 荒烟蔓草的年头
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=3)
add_instrument_note(instrument=melody, note_name='G3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)

# 就连分手都很沉
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='A2', range=2)

# 默
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=8)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='A2', range=4)

# 间奏balabala
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='G3', range=8)

add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=8)
add_instrument_note(instrument=melody, note_name='A3', range=1)
add_instrument_note(instrument=melody, note_name='G3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=3)
add_instrument_note(instrument=melody, note_name='D3', range=1)

add_instrument_note(instrument=melody, note_name='E3', range=3)
add_instrument_note(instrument=melody, note_name='G3', range=3)
add_instrument_note(instrument=melody, note_name='E3', range=10)

add_instrument_note(instrument=melody, note_name='A3', range=10)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=3)
add_instrument_note(instrument=melody, note_name='E3', range=1)

add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='A2', range=11)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)

add_instrument_note(instrument=melody, note_name='D3', range=10)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='A2', range=1)
add_instrument_note(instrument=melody, note_name='G2', range=2)
add_instrument_note(instrument=melody, note_name='A2', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=3)

add_instrument_note(instrument=melody, note_name='C3', range=14)

notes = change_notes_tempo(melody.notes, 15.0/initial_tempo)
melody.notes = notes

melody_c_melody.instruments.append(melody)

melody_c_melody.write('DongFengPo.midi')