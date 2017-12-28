# -*- coding: utf-8 -*-

import pretty_midi
from common import *

initial_tempo = 60.0
melody_c_melody = pretty_midi.PrettyMIDI(initial_tempo=initial_tempo)

###################################################### melody
melody_program = pretty_midi.instrument_name_to_program('Guitar harmonics')
melody = pretty_midi.Instrument(program = melody_program)

# 屋檐如悬崖风铃如沧海
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=3)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=3)

# 我等燕归来
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=3)
add_instrument_note(instrument=melody, note_name='A2', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=8)

# 时间被安排演一场意外
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=3)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=3)

# 你悄然走开
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=3)
add_instrument_note(instrument=melody, note_name='D3', range=8)

# 故事在城外浓雾散不开
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=3)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=3)

# 看不清对白
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=3)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=8)

# 你听不出来风声不存在
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=3)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=3)

# 是我在感慨
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=3)
add_instrument_note(instrument=melody, note_name='A3', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=9)

# 梦醒来是谁在窗台
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=1)
add_instrument_note(instrument=melody, note_name='G3', range=3)
add_instrument_note(instrument=melody, note_name='F3', range=1)
add_instrument_note(instrument=melody, note_name='F3', range=3)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=2)

# 把结局打开
add_instrument_note(instrument=melody, note_name='F3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='F3', range=3)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=8)

# 那薄如蝉翼的未来
add_instrument_note(instrument=melody, note_name='F3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=1)
add_instrument_note(instrument=melody, note_name='F3', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=3)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)

# 经不起谁来拆我
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=3)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=5)
add_instrument_note(instrument=melody, note_name='G3', range=1)

# 送你离开千里之外
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=3)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=3)

# 你无声黑白
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=3)
add_instrument_note(instrument=melody, note_name='E4', range=8)

# 沉默年代或许不该
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=3)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=3)

# 太遥远的相爱我
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=3)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=5)
add_instrument_note(instrument=melody, note_name='G3', range=1)

# 送你离开天涯之外
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=3)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=3)

# 你是否还在
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=3)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=8)

# 琴声何来生死难猜
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=3)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=3)

# 用一生去等待
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=9)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=17)

# 闻泪声入林寻梨花白只得一行青苔
add_instrument_note(instrument=melody, note_name='0', range=1)
add_instrument_note(instrument=melody, note_name='G2', range=1)
add_instrument_note(instrument=melody, note_name='G2', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='G2', range=1)
add_instrument_note(instrument=melody, note_name='G2', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='G2', range=1)
add_instrument_note(instrument=melody, note_name='G2', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=2)

# 天在山之外雨落花台我两鬓斑白
add_instrument_note(instrument=melody, note_name='0', range=1)
add_instrument_note(instrument=melody, note_name='G2', range=1)
add_instrument_note(instrument=melody, note_name='G2', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='G2', range=1)
add_instrument_note(instrument=melody, note_name='G2', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='G2', range=1)
add_instrument_note(instrument=melody, note_name='G2', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)

# 闻泪声入林寻梨花白只得一行青苔
add_instrument_note(instrument=melody, note_name='0', range=1)
add_instrument_note(instrument=melody, note_name='G2', range=1)
add_instrument_note(instrument=melody, note_name='G2', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='G2', range=1)
add_instrument_note(instrument=melody, note_name='G2', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='G2', range=1)
add_instrument_note(instrument=melody, note_name='G2', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=2)

# 天在山之外雨落花台我等你来
add_instrument_note(instrument=melody, note_name='0', range=1)
add_instrument_note(instrument=melody, note_name='G2', range=1)
add_instrument_note(instrument=melody, note_name='G2', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='G2', range=1)
add_instrument_note(instrument=melody, note_name='G2', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='G2', range=1)
add_instrument_note(instrument=melody, note_name='G2', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=4)

# 一身琉璃白透明着尘埃
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=3)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=3)

# 你无暇的爱
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=3)
add_instrument_note(instrument=melody, note_name='A2', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=8)

# 你从雨中来诗化了悲哀
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=3)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=3)

# 我淋湿现在
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=3)
add_instrument_note(instrument=melody, note_name='D3', range=8)

# 芙蓉水面采船行影犹在
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=3)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=3)

# 你却不回来
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=3)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=8)

# 被岁月覆盖你说的花开
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=3)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=3)

# 过去成空白
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=3)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=9)

# 梦醒来是谁在窗台
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=1)
add_instrument_note(instrument=melody, note_name='G3', range=3)
add_instrument_note(instrument=melody, note_name='F3', range=1)
add_instrument_note(instrument=melody, note_name='F3', range=3)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=2)

# 把结局打开
add_instrument_note(instrument=melody, note_name='F3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='F3', range=3)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=8)

# 那薄如蝉翼的未来
add_instrument_note(instrument=melody, note_name='F3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=1)
add_instrument_note(instrument=melody, note_name='F3', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=3)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)

# 经不起谁来拆我
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=3)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=5)
add_instrument_note(instrument=melody, note_name='G3', range=1)

# 送你离开千里之外
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=3)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=3)

# 你无声黑白
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=3)
add_instrument_note(instrument=melody, note_name='E4', range=8)

# 沉默年代或许不该
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=3)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=3)

# 太遥远的相爱我
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=3)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=5)
add_instrument_note(instrument=melody, note_name='G3', range=1)

# 送你离开天涯之外
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=3)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=3)

# 你是否还在
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=3)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=8)

# 琴声何来生死难猜
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=3)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=3)

# 用一生我
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=9)
add_instrument_note(instrument=melody, note_name='0', range=3)
add_instrument_note(instrument=melody, note_name='G3', range=1)

# 送你离开千里之外
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=3)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=3)

# 你无声黑白
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=3)
add_instrument_note(instrument=melody, note_name='E4', range=8)

# 沉默年代或许不该
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=3)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=3)

# 太遥远的相爱我
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=3)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=5)
add_instrument_note(instrument=melody, note_name='G3', range=1)

# 送你离开天涯之外
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=3)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=3)

# 你是否还在
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=3)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=8)

# 琴声何来生死难猜
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=3)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=3)

# 用一生去等待
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=9)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=17)

notes = change_notes_tempo(melody.notes, 15.0/initial_tempo)
melody.notes = notes

melody_c_melody.instruments.append(melody)

melody_c_melody.write('QianLiZhiWai.midi')