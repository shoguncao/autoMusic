# -*- coding: utf-8 -*-

import pretty_midi
from common import *

initial_tempo = 76.0
melody_c_melody = pretty_midi.PrettyMIDI(initial_tempo=initial_tempo)

###################################################### melody
melody_program = pretty_midi.instrument_name_to_program('Guitar harmonics')
melody = pretty_midi.Instrument(program = melody_program)

# 忽然之间
add_instrument_note(instrument=melody, note_name='0', range=4)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 天昏地暗
add_instrument_note(instrument=melody, note_name='0', range=4)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 世界可以忽然什么
add_instrument_note(instrument=melody, note_name='0', range=4)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='G2', range=2)
add_instrument_note(instrument=melody, note_name='F2', range=2)
add_instrument_note(instrument=melody, note_name='E2', range=1)

# 都没有
add_instrument_note(instrument=melody, note_name='F2', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=5)
add_instrument_note(instrument=melody, note_name='0', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 我想起了你
add_instrument_note(instrument=melody, note_name='0', range=3)
add_instrument_note(instrument=melody, note_name='G2', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 再想到自己
add_instrument_note(instrument=melody, note_name='0', range=3)
add_instrument_note(instrument=melody, note_name='G2', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 我为什么总在非常脆弱
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='G2', range=1)
add_instrument_note(instrument=melody, note_name='G2', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='G2', range=2)
add_instrument_note(instrument=melody, note_name='F2', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=1)

# 的时候，怀念
add_instrument_note(instrument=melody, note_name='F2', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=5)
add_instrument_note(instrument=melody, note_name='0', range=4)
add_instrument_note(instrument=melody, note_name='G2', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)

# 你。我明
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=8)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=2)

# 白，太放不开你的爱
add_instrument_note(instrument=melody, note_name='G3', range=4)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=1)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=3)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=5)

# 太熟悉你的关怀
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=3)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='B2', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=5)

# 分不开，想你算
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='G3', range=5)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='F3', range=2)

# 是安慰还是悲哀，而现在
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='F3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='F3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=1)
add_instrument_note(instrument=melody, note_name='G3', range=5)

# 就算时针都停摆
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=1)
add_instrument_note(instrument=melody, note_name='G3', range=3)
add_instrument_note(instrument=melody, note_name='F3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=5)

# 就算生命像尘埃
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=3)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='B2', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=5)

# 分不开，我们也
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='G3', range=5)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='F3', range=2)

# 许反而更相信爱
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='F3', range=1)
add_instrument_note(instrument=melody, note_name='A2', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 如果这天地
add_instrument_note(instrument=melody, note_name='0', range=3)
add_instrument_note(instrument=melody, note_name='G2', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 最终会消失
add_instrument_note(instrument=melody, note_name='0', range=3)
add_instrument_note(instrument=melody, note_name='G2', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 不想一路走来珍惜
add_instrument_note(instrument=melody, note_name='0', range=2)
add_instrument_note(instrument=melody, note_name='G2', range=1)
add_instrument_note(instrument=melody, note_name='G2', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='G2', range=2)
add_instrument_note(instrument=melody, note_name='F2', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=1)

# 的回忆，没有
add_instrument_note(instrument=melody, note_name='F2', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=5)
add_instrument_note(instrument=melody, note_name='0', range=4)
add_instrument_note(instrument=melody, note_name='G2', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)

# 你。我明
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=8)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=2)

# 白，太放不开你的爱
add_instrument_note(instrument=melody, note_name='G3', range=4)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=1)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=3)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=5)

# 太熟悉你的关怀
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=3)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='B2', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=5)

# 分不开，想你算
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='G3', range=5)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='F3', range=2)

# 是安慰还是悲哀，而现在
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='F3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='F3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=1)
add_instrument_note(instrument=melody, note_name='G3', range=5)

# 就算时针都停摆
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=1)
add_instrument_note(instrument=melody, note_name='G3', range=3)
add_instrument_note(instrument=melody, note_name='F3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=5)

# 就算生命像尘埃
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=3)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='B2', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=5)

# 分不开，我们也
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='G3', range=5)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='F3', range=2)

# 许反而更相信爱
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='F3', range=1)
add_instrument_note(instrument=melody, note_name='A2', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=4)
add_instrument_note(instrument=melody, note_name='0', range=4)

# 我明
add_instrument_note(instrument=melody, note_name='0', range=12)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=2)

# 白，太放不开你的爱
add_instrument_note(instrument=melody, note_name='G3', range=4)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=1)
add_instrument_note(instrument=melody, note_name='G3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=3)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=5)

# 太熟悉你的关怀
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=3)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='B2', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=5)

# 分不开，想你算
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='G3', range=5)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='F3', range=2)

# 是安慰还是悲哀，而现在
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='F3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='F3', range=2)
add_instrument_note(instrument=melody, note_name='G3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='D3', range=4)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=1)
add_instrument_note(instrument=melody, note_name='G3', range=5)

# 就算时针都停摆
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='F3', range=1)
add_instrument_note(instrument=melody, note_name='G3', range=3)
add_instrument_note(instrument=melody, note_name='F3', range=2)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=5)

# 就算生命像尘埃
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=3)
add_instrument_note(instrument=melody, note_name='D3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='B2', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=5)

# 分不开，我们也
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='G3', range=5)
add_instrument_note(instrument=melody, note_name='C3', range=2)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='F3', range=2)

# 许反而更相信爱
add_instrument_note(instrument=melody, note_name='E3', range=1)
add_instrument_note(instrument=melody, note_name='F3', range=1)
add_instrument_note(instrument=melody, note_name='A2', range=1)
add_instrument_note(instrument=melody, note_name='E3', range=2)
add_instrument_note(instrument=melody, note_name='D3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=1)
add_instrument_note(instrument=melody, note_name='C3', range=8)

notes = change_notes_tempo(melody.notes, 15.0/initial_tempo)
melody.notes = notes

melody_c_melody.instruments.append(melody)

melody_c_melody.write('HuRanZhiJian.midi')