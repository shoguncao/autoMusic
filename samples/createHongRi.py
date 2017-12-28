# -*- coding: utf-8 -*-

import pretty_midi
from common import *

initial_tempo = 76.0
melody_c_melody = pretty_midi.PrettyMIDI(initial_tempo=initial_tempo)

###################################################### melody
melody_program = pretty_midi.instrument_name_to_program('Guitar harmonics')
melody = pretty_midi.Instrument(program = melody_program)

# 命运就算颠沛流离
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='G2', range=2)
add_instrument_note(instrument=melody, note_name='G2', range=2)

# 命运就算曲折离奇
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='G2', range=2)
add_instrument_note(instrument=melody, note_name='G2', range=2)

# 命运就算恐吓着你
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='B2', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)

# 做人没趣味别流
add_instrument_note(instrument=melody, note_name='B2', range=2)
add_instrument_note(instrument=melody, note_name='A2', range=2)
add_instrument_note(instrument=melody, note_name='B2', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='B2', range=4)
add_instrument_note(instrument=melody, note_name='A2', range=2)
add_instrument_note(instrument=melody, note_name='G2', range=2)

# 泪心酸更不
add_instrument_note(instrument=melody, note_name='A2', range=4)
add_instrument_note(instrument=melody, note_name='A3', range=4)
add_instrument_note(instrument=melody, note_name='G3', range=4)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=2)

# 应舍弃我愿
add_instrument_note(instrument=melody, note_name='E3', range=4)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='B2', range=2)

# 能一生永远陪伴
add_instrument_note(instrument=melody, note_name='A2', range=4)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='B2', range=2)
add_instrument_note(instrument=melody, note_name='A2', range=2)
add_instrument_note(instrument=melody, note_name='B2', range=2)

# 你
add_instrument_note(instrument=melody, note_name='C3', range=12)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 命运就算颠沛流离
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='G2', range=2)
add_instrument_note(instrument=melody, note_name='G2', range=2)

# 命运就算曲折离奇
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='G2', range=2)
add_instrument_note(instrument=melody, note_name='G2', range=2)

# 命运就算恐吓着你
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='B2', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)

# 做人没趣味别流
add_instrument_note(instrument=melody, note_name='B2', range=2)
add_instrument_note(instrument=melody, note_name='A2', range=2)
add_instrument_note(instrument=melody, note_name='B2', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='B2', range=4)
add_instrument_note(instrument=melody, note_name='A2', range=2)
add_instrument_note(instrument=melody, note_name='G2', range=2)

# 泪心酸更不
add_instrument_note(instrument=melody, note_name='A2', range=4)
add_instrument_note(instrument=melody, note_name='A3', range=4)
add_instrument_note(instrument=melody, note_name='G3', range=4)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=2)

# 应舍弃我愿
add_instrument_note(instrument=melody, note_name='E3', range=4)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='B2', range=2)

# 能一生永远陪伴
add_instrument_note(instrument=melody, note_name='A2', range=4)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='B2', range=2)
add_instrument_note(instrument=melody, note_name='A2', range=2)
add_instrument_note(instrument=melody, note_name='B2', range=2)

# 你
add_instrument_note(instrument=melody, note_name='C3', range=12)
add_instrument_note(instrument=melody, note_name='0', range=4)

# AH
add_instrument_note(instrument=melody, note_name='E3', range=8)
add_instrument_note(instrument=melody, note_name='D3', range=8)

# AH
add_instrument_note(instrument=melody, note_name='D3', range=3)
add_instrument_note(instrument=melody, note_name='G3', range=3)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='B2', range=4)

# AH
add_instrument_note(instrument=melody, note_name='A2', range=4)
add_instrument_note(instrument=melody, note_name='B2', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=6)
add_instrument_note(instrument=melody, note_name='C3', range=2)

# AH
add_instrument_note(instrument=melody, note_name='C3', range=12)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 一生之中兜兜转转
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)

# 哪会看清楚彷徨时
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='G2', range=2)
add_instrument_note(instrument=melody, note_name='G2', range=2)
add_instrument_note(instrument=melody, note_name='G2', range=2)

# 我也试过独坐一角
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)

# 像是没协助
add_instrument_note(instrument=melody, note_name='B2', range=2)
add_instrument_note(instrument=melody, note_name='B2', range=2)
add_instrument_note(instrument=melody, note_name='B2', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='B2', range=8)

# 在某年那幼
add_instrument_note(instrument=melody, note_name='A2', range=4)
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='A2', range=4)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)

# 小的我跌倒过
add_instrument_note(instrument=melody, note_name='E3', range=4)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)

# 几多几多落泪在雨
add_instrument_note(instrument=melody, note_name='F3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=2)

# 夜滂沱
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='D3', range=10)

# 一生之中弯弯曲曲
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)

# 我也要走过从何时
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='G2', range=2)
add_instrument_note(instrument=melody, note_name='G2', range=3)
add_instrument_note(instrument=melody, note_name='G2', range=1)

# 有你有你伴我给我
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)

# 热烈的拍和像红
add_instrument_note(instrument=melody, note_name='B2', range=2)
add_instrument_note(instrument=melody, note_name='B2', range=2)
add_instrument_note(instrument=melody, note_name='B2', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='B2', range=4)
add_instrument_note(instrument=melody, note_name='A2', range=2)
add_instrument_note(instrument=melody, note_name='G2', range=2)

# 日之火点燃
add_instrument_note(instrument=melody, note_name='A2', range=4)
add_instrument_note(instrument=melody, note_name='A3', range=4)
add_instrument_note(instrument=melody, note_name='G3', range=4)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=2)

# 真的我结伴
add_instrument_note(instrument=melody, note_name='E3', range=4)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='B2', range=2)

# 行千山也定能踏
add_instrument_note(instrument=melody, note_name='A2', range=4)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='B2', range=2)
add_instrument_note(instrument=melody, note_name='A2', range=2)
add_instrument_note(instrument=melody, note_name='B2', range=2)

# 过让晚风
add_instrument_note(instrument=melody, note_name='C3', range=8)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=4)
add_instrument_note(instrument=melody, note_name='G3', range=10)

# 轻轻吹
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=4)

# 过伴送着
add_instrument_note(instrument=melody, note_name='C3', range=6)
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)

# 清幽花香像是在祝
add_instrument_note(instrument=melody, note_name='F3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=2)

# 福你我让晚
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=4)

# 星轻轻吹
add_instrument_note(instrument=melody, note_name='G3', range=8)
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=4)

# 过闪出你
add_instrument_note(instrument=melody, note_name='C3', range=6)
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)

# 每个希冀如浪花
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=3)
add_instrument_note(instrument=melody, note_name='D3', range=3)
add_instrument_note(instrument=melody, note_name='A3', range=6)

# 快要沾湿
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=4)

# 我 Wo
add_instrument_note(instrument=melody, note_name='D3', range=12)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=1)

# Wo
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='G3', range=11)
add_instrument_note(instrument=melody, note_name='0', range=4)

add_instrument_note(instrument=melody, note_name='0', range=16)

# 命运就算颠沛流离
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='G2', range=2)
add_instrument_note(instrument=melody, note_name='G2', range=2)

# 命运就算曲折离奇
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='G2', range=2)
add_instrument_note(instrument=melody, note_name='G2', range=2)

# 命运就算恐吓着你
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='B2', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)

# 做人没趣味别流
add_instrument_note(instrument=melody, note_name='B2', range=2)
add_instrument_note(instrument=melody, note_name='A2', range=2)
add_instrument_note(instrument=melody, note_name='B2', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='B2', range=4)
add_instrument_note(instrument=melody, note_name='A2', range=2)
add_instrument_note(instrument=melody, note_name='G2', range=2)

# 泪心酸更不
add_instrument_note(instrument=melody, note_name='A2', range=4)
add_instrument_note(instrument=melody, note_name='A3', range=4)
add_instrument_note(instrument=melody, note_name='G3', range=4)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=2)

# 应舍弃我愿
add_instrument_note(instrument=melody, note_name='E3', range=4)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='B2', range=2)

# 能一生永远陪伴
add_instrument_note(instrument=melody, note_name='A2', range=4)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='B2', range=2)
add_instrument_note(instrument=melody, note_name='A2', range=2)
add_instrument_note(instrument=melody, note_name='B2', range=2)

# 你
add_instrument_note(instrument=melody, note_name='C3', range=16)

notes = change_notes_tempo(melody.notes, 15.0/initial_tempo)
melody.notes = notes

melody_c_melody.instruments.append(melody)

melody_c_melody.write('HongRi.midi')