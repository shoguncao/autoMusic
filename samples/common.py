# -*- coding: utf-8 -*-

import pretty_midi

StrongestVelocity = 100	# 第一拍强拍 强度
StrongerVelocity = 100	# 第三拍次强拍 强度
WeakVelocity = 100 # 第二、四弱拍 强度

def change_notes_tempo(notes, rate):
	# 将速度放慢rate倍
	notes = sorted(notes, key=lambda x:x.start)
	for note in notes:
		note.start = note.start*rate
		note.end = note.end*rate
	return notes

def print_notes(notes):
	# 打印notes
	for note in notes:
		print 'pitch: ', note.pitch, ', start: ', note.start, ', end: ', note.end

EndTime = 0
def add_instrument_note(instrument, note_name, start=0, range=0):
	# 在当前melody的基础上，增加一个note_name的音，其延续时间为range
	global EndTime
	quater = int(instrument.get_end_time()/0.25) % 4 # 在一个小节中的第几拍
	velocity = WeakVelocity
	if 0 == quater:
		velocity = StrongestVelocity
	if 2 == quater:
		velocity = StrongerVelocity
	if 0 == start:
		start = EndTime
	EndTime = start + range
	if '0' != note_name:
		pitch = pretty_midi.note_name_to_number(note_name)
		note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start+range)
		instrument.notes.append(note)
	