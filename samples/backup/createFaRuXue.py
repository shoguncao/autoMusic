# -*- coding: utf-8 -*-

import pretty_midi
from common import *

initial_tempo = 56.0
melody_c_melody = pretty_midi.PrettyMIDI(initial_tempo=initial_tempo)

###################################################### melody
melody_program = pretty_midi.instrument_name_to_program('Guitar harmonics')
melody = pretty_midi.Instrument(program = melody_program)

# 前奏
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=1)
add_instrument_note(instrument=melody, note_name='A4', range=1)
add_instrument_note(instrument=melody, note_name='C5', range=2)
add_instrument_note(instrument=melody, note_name='E5', range=2)
add_instrument_note(instrument=melody, note_name='D5', range=3)
add_instrument_note(instrument=melody, note_name='E5', range=1)
add_instrument_note(instrument=melody, note_name='D5', range=2)
add_instrument_note(instrument=melody, note_name='C5', range=2)

add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=1)
add_instrument_note(instrument=melody, note_name='A4', range=1)
add_instrument_note(instrument=melody, note_name='C5', range=2)
add_instrument_note(instrument=melody, note_name='E5', range=2)
add_instrument_note(instrument=melody, note_name='D5', range=3)
add_instrument_note(instrument=melody, note_name='G5', range=1)
add_instrument_note(instrument=melody, note_name='E5', range=2)
add_instrument_note(instrument=melody, note_name='C5', range=2)

# 狼牙月依人憔悴
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=5)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='G4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=3)

# 我举杯饮尽了风雪
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=5)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='A4', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=5)

# 是谁打翻前世
add_instrument_note(instrument=melody, note_name='0', range=3)
add_instrument_note(instrument=melody, note_name='A3', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=3)
add_instrument_note(instrument=melody, note_name='A3', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=2)

# 柜惹尘埃是非
add_instrument_note(instrument=melody, note_name='D4', range=3)
add_instrument_note(instrument=melody, note_name='0', range=3)
add_instrument_note(instrument=melody, note_name='A3', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=3)

# 缘字诀几番轮回
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=5)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='G4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=3)

# 你锁眉哭红颜唤不回
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=4)
add_instrument_note(instrument=melody, note_name='G3', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='A4', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=5)

# 纵然青史已经
add_instrument_note(instrument=melody, note_name='0', range=3)
add_instrument_note(instrument=melody, note_name='A3', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=3)
add_instrument_note(instrument=melody, note_name='A3', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=3)

# 成灰我爱不灭
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=5)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=7)

# 繁华如三千东流水
add_instrument_note(instrument=melody, note_name='A3', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='A3', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=3)
add_instrument_note(instrument=melody, note_name='A3', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=3)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=5)

# 我只取一瓢爱了解
add_instrument_note(instrument=melody, note_name='A3', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='A3', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=3)
add_instrument_note(instrument=melody, note_name='A3', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=5)

# 只恋你化身的蝶
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='A4', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=9)

# 你发如雪
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=3)

# 凄美了离别我焚
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=3)
add_instrument_note(instrument=melody, note_name='G4', range=1)
add_instrument_note(instrument=melody, note_name='A4', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=3)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=2)

# 香感动了谁邀明
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='A4', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='G4', range=5)
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=1)
add_instrument_note(instrument=melody, note_name='A4', range=1)

# 月让回忆皎洁爱在
add_instrument_note(instrument=melody, note_name='C5', range=4)
add_instrument_note(instrument=melody, note_name='A4', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=3)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=1)

# 月光下完美你发如雪
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=3)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=3)

# 纷飞了眼泪我等
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=3)
add_instrument_note(instrument=melody, note_name='G4', range=1)
add_instrument_note(instrument=melody, note_name='A4', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=3)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=2)

# 待苍老了谁红尘
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='A4', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='G4', range=5)
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=1)
add_instrument_note(instrument=melody, note_name='A4', range=1)

# 醉微醺的岁月我
add_instrument_note(instrument=melody, note_name='C5', range=4)
add_instrument_note(instrument=melody, note_name='A4', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=4)
add_instrument_note(instrument=melody, note_name='C4', range=1)

# 用无悔刻永世爱你的
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=4)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=2)

# 碑
add_instrument_note(instrument=melody, note_name='C4', range=7)
add_instrument_note(instrument=melody, note_name='0', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 间奏
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=1)
add_instrument_note(instrument=melody, note_name='A4', range=1)
add_instrument_note(instrument=melody, note_name='C5', range=2)
add_instrument_note(instrument=melody, note_name='G5', range=2)
add_instrument_note(instrument=melody, note_name='C5', range=1)
add_instrument_note(instrument=melody, note_name='C5', range=1)
add_instrument_note(instrument=melody, note_name='C5', range=1)
add_instrument_note(instrument=melody, note_name='G5', range=1)
add_instrument_note(instrument=melody, note_name='E5', range=1)
add_instrument_note(instrument=melody, note_name='D5', range=1)
add_instrument_note(instrument=melody, note_name='C5', range=2)

add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=1)
add_instrument_note(instrument=melody, note_name='A4', range=1)
add_instrument_note(instrument=melody, note_name='C5', range=2)
add_instrument_note(instrument=melody, note_name='E5', range=2)
add_instrument_note(instrument=melody, note_name='D5', range=1)
add_instrument_note(instrument=melody, note_name='D5', range=1)
add_instrument_note(instrument=melody, note_name='D5', range=1)
add_instrument_note(instrument=melody, note_name='G5', range=1)
add_instrument_note(instrument=melody, note_name='E5', range=2)
add_instrument_note(instrument=melody, note_name='C5', range=2)

# 哦
add_instrument_note(instrument=melody, note_name='C5', range=1)
add_instrument_note(instrument=melody, note_name='C5', range=1)
add_instrument_note(instrument=melody, note_name='C5', range=1)
add_instrument_note(instrument=melody, note_name='C5', range=1)
add_instrument_note(instrument=melody, note_name='0', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)

# 狼牙月依人憔悴
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=5)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='G4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=3)

# 我举杯饮尽了风雪
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=5)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='A4', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=5)

# 是谁打翻前世
add_instrument_note(instrument=melody, note_name='0', range=3)
add_instrument_note(instrument=melody, note_name='A3', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=3)
add_instrument_note(instrument=melody, note_name='A3', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=2)

# 柜惹尘埃是非
add_instrument_note(instrument=melody, note_name='D4', range=3)
add_instrument_note(instrument=melody, note_name='0', range=3)
add_instrument_note(instrument=melody, note_name='A3', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=3)

# 缘字诀几番轮回
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=5)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='G4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=3)

# 你锁眉哭红颜唤不回
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=4)
add_instrument_note(instrument=melody, note_name='G3', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='A4', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=5)

# 纵然青史已经
add_instrument_note(instrument=melody, note_name='0', range=3)
add_instrument_note(instrument=melody, note_name='A3', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=3)
add_instrument_note(instrument=melody, note_name='A3', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=3)

# 成灰我爱不灭
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=5)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=7)

# 繁华如三千东流水
add_instrument_note(instrument=melody, note_name='A3', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='A3', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=3)
add_instrument_note(instrument=melody, note_name='A3', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=3)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=5)

# 我只取一瓢爱了解
add_instrument_note(instrument=melody, note_name='A3', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='A3', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=3)
add_instrument_note(instrument=melody, note_name='A3', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=5)

# 只恋你化身的蝶
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='A4', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=9)

# 你发如雪
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=3)

# 凄美了离别我焚
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=3)
add_instrument_note(instrument=melody, note_name='G4', range=1)
add_instrument_note(instrument=melody, note_name='A4', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=3)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=2)

# 香感动了谁邀明
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='A4', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='G4', range=5)
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=1)
add_instrument_note(instrument=melody, note_name='A4', range=1)

# 月让回忆皎洁爱在
add_instrument_note(instrument=melody, note_name='C5', range=4)
add_instrument_note(instrument=melody, note_name='A4', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=3)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=1)

# 月光下完美你发如雪
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=3)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=3)

# 纷飞了眼泪我等
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=3)
add_instrument_note(instrument=melody, note_name='G4', range=1)
add_instrument_note(instrument=melody, note_name='A4', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=3)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=2)

# 待苍老了谁红尘
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='A4', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='G4', range=5)
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=1)
add_instrument_note(instrument=melody, note_name='A4', range=1)

# 醉微醺的岁月我
add_instrument_note(instrument=melody, note_name='C5', range=4)
add_instrument_note(instrument=melody, note_name='A4', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=4)
add_instrument_note(instrument=melody, note_name='C4', range=1)

# 用无悔刻永世爱你的
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=4)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=2)

# 碑 你发如雪
add_instrument_note(instrument=melody, note_name='C4', range=7)
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=3)

# 凄美了离别我焚
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=3)
add_instrument_note(instrument=melody, note_name='G4', range=1)
add_instrument_note(instrument=melody, note_name='A4', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=3)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=2)

# 香感动了谁邀明
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='A4', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='G4', range=5)
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=1)
add_instrument_note(instrument=melody, note_name='A4', range=1)

# 月让回忆皎洁爱在
add_instrument_note(instrument=melody, note_name='C5', range=4)
add_instrument_note(instrument=melody, note_name='A4', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=3)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=1)

# 月光下完美你发如雪
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=3)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=3)

# 纷飞了眼泪我等
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=3)
add_instrument_note(instrument=melody, note_name='G4', range=1)
add_instrument_note(instrument=melody, note_name='A4', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=3)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=2)

# 待苍老了谁红尘
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='A4', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='G4', range=5)
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=1)
add_instrument_note(instrument=melody, note_name='A4', range=1)

# 醉微醺的岁月我
add_instrument_note(instrument=melody, note_name='C5', range=4)
add_instrument_note(instrument=melody, note_name='A4', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='G4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=4)
add_instrument_note(instrument=melody, note_name='C4', range=1)

# 用无悔刻永世爱你的
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=4)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=3)

# 碑
add_instrument_note(instrument=melody, note_name='C4', range=10)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 啦儿啦啦儿啦啦儿啦儿
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)

# 铜镜映无邪扎马尾
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=3)
add_instrument_note(instrument=melody, note_name='A3', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=2)

# 你若撒野今生我把酒奉陪
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)

# 啦儿啦啦儿啦啦儿啦儿啦
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='G4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=2)

# 啦儿啦啦儿啦啦儿啦儿
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)

# 铜镜映无邪扎马尾
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='A3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=3)
add_instrument_note(instrument=melody, note_name='A3', range=1)
add_instrument_note(instrument=melody, note_name='C4', range=2)
add_instrument_note(instrument=melody, note_name='D4', range=2)

# 你若撒野今生我把酒奉陪
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='E4', range=1)
add_instrument_note(instrument=melody, note_name='D4', range=1)
add_instrument_note(instrument=melody, note_name='E4', range=2)
add_instrument_note(instrument=melody, note_name='C4', range=2)

notes = change_notes_tempo(melody.notes, 15.0/initial_tempo)
melody.notes = notes

melody_c_melody.instruments.append(melody)

melody_c_melody.write('FaRuXue.midi')