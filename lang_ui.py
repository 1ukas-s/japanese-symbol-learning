
import os
import numpy as np
import time
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt, QTimer
import sys

accents = ["っ","ゝ","゛","゜"]

hiragana= [["あ", "い", "う", "え", "お"], #None
["か", "き", "く", "け", "こ", "きゃ", "きゅ", "きょ"], # K
["が", "ぎ", "ぐ", "げ", "ご", "ぎゃ", "ぎゅ", "ぎょ"], # G
["さ", "し", "す", "せ", "そ", "しゃ", "しゅ", "しょ"], # S
["ざ", "じ", "ず", "ぜ", "ぞ", "じゃ", "じゅ", "じょ"], # Z
["た", "ち", "つ", "て", "と", "ちゃ", "ちゅ", "ちょ"], # T
["だ", "ぢ", "づ", "で", "ど", "ぢゃ", "ぢゅ", "ぢょ"], # D
["な", "に", "ぬ", "ね", "の", "にゃ", "にゅ", "にょ"], # N
["は", "ひ", "ふ", "へ", "ほ", "ひゃ", "ひゅ", "ひょ"], # H
["ば", "び", "ぶ", "べ", "ぼ", "びゃ", "びゅ", "びょ"], # B
["ぱ", "ぴ", "ぷ", "ぺ", "ぽ", "ぴゃ", "ぴゅ", "ぴょ"], # P
["ま", "み", "む", "め", "も", "みゃ", "みゅ", "みょ"], # M
["や", "以", "ゆ", "𛀁", "よ"], # Y
["ら", "り", "る", "れ", "ろ", "りゃ", "りゅ", "りょ"], # R
["わ", "ゐ", "ゑ", "を"],			# W
["ん"]]		# N (No vowel)

hiragana_labels= [["<font size=5>あ</font>", "<font size=5>い</font>", "<font size=5>う</font>", "<font size=5>え</font>", "<font size=5>お</font>"], #None
["<font size=5><font size=5>か</font></font>", "<font size=5>き</font>", "<font size=5>く</font>", "<font size=5>け</font>", "<font size=5>こ</font>", "<font size=5>き</font><font size=4>ゃ</font>", "<font size=5>き</font><font size=4>ゅ</font>", "<font size=5>き</font><font size=4>ょ</font>"], # K
["<font size=5>が</font>", "<font size=5>ぎ</font>", "<font size=5>ぐ</font>", "<font size=5>げ</font>", "<font size=5>ご</font>", "<font size=5>ぎ</font><font size=4>ゃ</font>", "<font size=5>ぎ</font><font size=4>ゅ</font>", "<font size=5>ぎ</font><font size=4>ょ</font>"], # G
["<font size=5>さ</font>", "<font size=5>し</font>", "<font size=5>す</font>", "<font size=5>せ</font>", "<font size=5>そ</font>", "<font size=5>し</font><font size=4>ゃ</font>", "<font size=5>し</font><font size=4>ゅ</font>", "<font size=5>し</font><font size=4>ょ</font>"], # S
["<font size=5>ざ</font>", "<font size=5>じ</font>", "<font size=5>ず</font>", "<font size=5>ぜ</font>", "<font size=5>ぞ</font>", "<font size=5>じ</font><font size=4>ゃ</font>", "<font size=5>じ</font><font size=4>ゅ</font>", "<font size=5>じ</font><font size=4>ょ</font>"], # Z
["<font size=5>た</font>", "<font size=5>ち</font>", "<font size=5>つ</font>", "<font size=5>て</font>", "<font size=5>と</font>", "<font size=5>ち</font><font size=4>ゃ</font>", "<font size=5>ち</font><font size=4>ゅ</font>", "<font size=5>ち</font><font size=4>ょ</font>"], # T
["<font size=5>だ</font>", "<font size=5>ぢ</font>", "<font size=5>づ</font>", "<font size=5>で</font>", "<font size=5>ど</font>", "<font size=5>ぢ</font><font size=4>ゃ</font>", "<font size=5>ぢ</font><font size=4>ゅ</font>", "<font size=5>ぢ</font><font size=4>ょ</font>"], # D
["<font size=5>な</font>", "<font size=5>に</font>", "<font size=5>ぬ</font>", "<font size=5>ね</font>", "<font size=5>の</font>", "<font size=5>に</font><font size=4>ゃ</font>", "<font size=5>に</font><font size=4>ゅ</font>", "<font size=5>に</font><font size=4>ょ</font>"], # N
["<font size=5>は</font>", "<font size=5>ひ</font>", "<font size=5>ふ</font>", "<font size=5>へ</font>", "<font size=5>ほ</font>", "<font size=5>ひ</font><font size=4>ゃ</font>", "<font size=5>ひ</font><font size=4>ゅ</font>", "<font size=5>ひ</font><font size=4>ょ</font>"], # H
["<font size=5>ば</font>", "<font size=5>び</font>", "<font size=5>ぶ</font>", "<font size=5>べ</font>", "<font size=5>ぼ</font>", "<font size=5>び</font><font size=4>ゃ</font>", "<font size=5>び</font><font size=4>ゅ</font>", "<font size=5>び</font><font size=4>ょ</font>"], # B
["<font size=5>ぱ</font>", "<font size=5>ぴ</font>", "<font size=5>ぷ</font>", "<font size=5>ぺ</font>", "<font size=5>ぽ</font>", "<font size=5>ぴ</font><font size=4>ゃ</font>", "<font size=5>ぴ</font><font size=4>ゅ</font>", "<font size=5>ぴ</font><font size=4>ょ</font>"], # P
["<font size=5>ま</font>", "<font size=5>み</font>", "<font size=5>む</font>", "<font size=5>め</font>", "<font size=5>も</font>", "<font size=5>み</font><font size=4>ゃ</font>", "<font size=5>み</font><font size=4>ゅ</font>", "<font size=5>み</font><font size=4>ょ</font>"], # M
["<font size=5>や</font>", "<font size=5>以</font>", "<font size=5>ゆ</font>", "<font size=5>𛀁</font>", "<font size=5>よ</font>"], # Y
["<font size=5>ら</font>", "<font size=5>り</font>", "<font size=5>る</font>", "<font size=5>れ</font>", "<font size=5>ろ</font>", "<font size=5>り</font><font size=4>ゃ</font>", "<font size=5>り</font><font size=4>ゅ</font>", "<font size=5>り</font><font size=4>ょ</font>"], # R
["<font size=5>わ</font>", "<font size=5>ゐ</font>", "<font size=5>ゑ</font>", "<font size=5>を</font>"],			# W
["<font size=5>ん</font>"]]		# N (No vowel)

romaji= [["a","i","u","e","o"], #None
["ka","ki","ku","ke","ko", "kya", "kyu", "kyo"], # K
["ga", "gi", "gu", "ge", "go", "gya", "gyu", "gyo"], # G
["sa","shi","su","se","so", "sha", "shu", "sho"], # S
["za", "ji", "zu", "ze", "zo", "ja", "ju", "jo"], # Z
["ta","chi","tsu","te","to", "cha", "chu", "cho"], # T
["da", "ji", "zu", "de", "do", "ja", "ju", "jo"], # D
["na","ni","nu","ne","no", "nya", "nyu", "nyo"], # N
["ha","hi","fu","he","ho", "hya", "hyu", "hyo"], # H
["ba", "bi", "bu", "be", "bo", "bya", "byu", "byo"], # B
["pa", "pi", "pu", "pe", "po", "pya", "pyu", "pyo"], # P
["ma","mi","mu","me","mo", "mya", "myu", "myo"], # M
["ya","yi", "yu","ye", "yo"], # Y
["ra","ri","ru","re","ro", "rya", "ryu", "ryo"], # R
["wa","wi", "we","o"],			# W
["n"]]		# N (No vowel)

def indices_by_character(string, table):
	for (i1, subtable) in enumerate(table):
		for (i2, entry) in enumerate(subtable):
			if entry == string:
				return (i1, i2)
	return None

last_few = [0, 0, 0, 0, 0]
def generate_one(table, spec=0):
	global last_few
	rand1 = np.random.permutation(len(table))
	i = 0
	while last_few.count(rand1[i]) > 0 or ([2, 4, 6, 9, 10].count(rand1[i]) > 0 and spec > 1):
		i += 1
	rand2 = np.random.permutation(len(table[rand1[i]]))
	j = 0
	while [5, 6, 7].count(rand2[j]) > 0 and (spec == 1 or spec == 3):
		j += 1
	last_few.append(rand1[i])
	last_few.pop(0)
	return tuple([rand1[i], rand2[j]])

class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__()
		#QTimer.singleShot(1000, lambda: print("test"))
		self.widget = QWidget()
		self.layout = QGridLayout()
		self.settings = [True, False, 0, False, False, 3, False] # 0 - Starting Lang, 2 - Multiple Char, 3 - Kana, 4,5 - Time Attack
		self.stats = [0, 0, [], []]
		for i1 in range(0, len(hiragana)):
			self.stats[2].append([])
			self.stats[3].append([])
			for i2 in range(0, len(hiragana[i1])):
				self.stats[2][-1].append([hiragana[i1][i2], 0, 0])
				self.stats[3][-1].append([romaji[i1][i2], 0, 0])
		self.score = [0, 10, 3100]
		self.options = [QLabel("Settings"), QLabel(f"Max Kana: {self.settings[5]}"), QLabel(f"Right: {self.stats[0]}"), QLabel(f"Wrong: {self.stats[1]}")]
		self.keys = [[], []]
		self.keys[0] = [[QPushButton("") for entry in table] for table in hiragana_labels] # Table of character buttons
		self.keys[1] = [[QLabel(entry) for entry in table] for table in hiragana_labels] # Table of character labels
		self.questions = [QLabel("") for entry in range(0, 10)]
		self.answers = ["" for entry in range(0, 10)]
		self.decaying = [False for entry in range(0, 10)]
		self.text = QLabel("")
		self.result = QLabel("")
		self.options_buttons = [QPushButton("Hiragana"), # Table of settings buttons
						   QPushButton("Romaji"),
						   QPushButton("Single Characters"),
						   QPushButton("Many Characters"),
						   QPushButton("All Characters"),
						   QPushButton("No Digraphs"),
						   QPushButton("No Graphemes"),
						   QPushButton("Neither"),
						   QPushButton("Time Attack"),
						   QPushButton("↑"),
						   QPushButton("↓"),
						   QPushButton("Start"),
						   QPushButton("Reset Stats"),
						   QPushButton("End"),
						   QPushButton("Print Stats"),
						   QPushButton("Hide Keyboard")]
		for i in range(0, len(self.keys[0])-1): # Change button/label settings for the hiragana keyboard
			for j in range(0, len(self.keys[0][i])):
				self.keys[1][i][j].setAttribute(Qt.WA_TranslucentBackground) # Make QLabel transparent
				self.keys[1][i][j].setAttribute(Qt.WA_TransparentForMouseEvents) # Make QLabel click-through
				self.keys[1][i][j].setAlignment(Qt.AlignCenter)
				self.keys[1][i][j].setFixedWidth(45)
				self.keys[1][i][j].setFixedHeight(35)
				self.keys[0][i][j].setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
				self.keys[0][i][j].setFixedWidth(45)
				self.keys[0][i][j].setFixedHeight(35)
				self.keys[0][i][j].setFocusPolicy(Qt.NoFocus)
				self.layout.addWidget(self.keys[0][i][j], i+3, j)
				self.layout.addWidget(self.keys[1][i][j], i+3, j)
				self.keys[0][i][j].clicked.connect(lambda _=None, i=i, j=j: self.text.setText(self.text.text() + hiragana[i][j]))

		self.keys[1][-1][0].setAttribute(Qt.WA_TranslucentBackground) # Same settings for ん character
		self.keys[1][-1][0].setAttribute(Qt.WA_TransparentForMouseEvents)
		self.keys[1][-1][0].setAlignment(Qt.AlignCenter)
		self.keys[1][-1][0].setFixedWidth(45)
		self.keys[1][-1][0].setFixedHeight(35)
		self.keys[0][-1][0].setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
		self.keys[0][-1][0].setFixedWidth(45)
		self.keys[0][-1][0].setFixedHeight(35)
		self.keys[0][-1][0].setFocusPolicy(Qt.NoFocus)
		self.layout.addWidget(self.keys[0][-1][0], 3, 7)
		self.layout.addWidget(self.keys[1][-1][0], 3, 7) # put ん label and button on top line
		self.keys[0][-1][0].clicked.connect(lambda: self.text.setText(self.text.text() + hiragana[-1][0]))

		self.options[0].setAlignment(Qt.AlignCenter)
		self.options[1].setAlignment(Qt.AlignCenter)
		self.options[2].setAlignment(Qt.AlignCenter)
		self.options[3].setAlignment(Qt.AlignCenter)
		self.layout.addWidget(self.options[0], 13, 12, 1, 3) # Settings text
		self.layout.addWidget(self.options[1], 16, 15, 1, 3) # Max Kana text
		self.layout.addWidget(self.options[2], 5, 9, 1, 3) # Score
		self.layout.addWidget(self.options[3], 5, 12, 1, 3)
		self.layout.addWidget(QLabel(" 	  "), 14, 8)
		for i in range(0, len(self.options_buttons)-6): # Settings buttons
			self.options_buttons[i].setFixedHeight(35)
			self.options_buttons[i].setFocusPolicy(Qt.NoFocus)
			self.layout.addWidget(self.options_buttons[i], 14+(i%4), 9+3*(round(((i+0.01)/4)-0.5)%4), 1, 3)
			self.options_buttons[i].clicked.connect(lambda _=None, m=i: self.options_button(m))

		self.layout.addWidget(self.options_buttons[11], 4, 9, 1, 3)
		self.layout.addWidget(self.options_buttons[12], 4, 12, 1, 3)
		self.layout.addWidget(self.options_buttons[13], 4, 15, 1, 3)
		self.layout.addWidget(self.options_buttons[14], 5, 15, 1, 3)
		self.layout.addWidget(self.options_buttons[15], 13, 15, 1, 3)


		self.options_buttons[10].setFocusPolicy(Qt.NoFocus)
		self.options_buttons[11].setFocusPolicy(Qt.NoFocus)
		self.options_buttons[12].setFocusPolicy(Qt.NoFocus)
		self.options_buttons[13].setFocusPolicy(Qt.NoFocus)
		self.options_buttons[14].setFocusPolicy(Qt.NoFocus)
		self.options_buttons[15].setFocusPolicy(Qt.NoFocus)

		self.options_buttons[11].clicked.connect(lambda: self.options_button(11))
		self.options_buttons[12].clicked.connect(lambda: self.options_button(12))
		self.options_buttons[13].clicked.connect(lambda: self.options_button(13))
		self.options_buttons[14].clicked.connect(lambda: self.options_button(14))
		self.options_buttons[15].clicked.connect(lambda: self.options_button(15))

		self.options_buttons[11].setEnabled(False)
		self.options_buttons[13].setEnabled(False)
		self.options_buttons[14].setEnabled(False)
		self.layout.addWidget(self.options_buttons[10], 17, 15, 1, 3)
		self.options_buttons[10].clicked.connect(lambda: self.options_button(10))
		self.options_buttons[0].setFlat(True)
		self.options_buttons[2].setFlat(True)
		self.options_buttons[4].setFlat(True)

		for i in range(0, len(self.questions)):
			self.layout.addWidget(self.questions[i], 8, i+9)
		self.text.setAlignment(Qt.AlignCenter)
		self.result.setAlignment(Qt.AlignCenter)
		self.layout.addWidget(self.text, 11, 9, 1, 9)
		self.layout.addWidget(self.result, 6, 9, 2, 9)
		self.layout.setSpacing(0)
		self.widget.setLayout(self.layout)
		self.setCentralWidget(self.widget)
		self.setGeometry(100, 100, 1000, 400)
		self.setWindowTitle("Japanese Alphabet Test")

	def keyPressEvent(self, e):
		text = self.text.text()
		#print(e.key())
		#print(e.text())
		if e.key() == 16777219:
			self.text.setText(text[0:-1])
		elif e.key() == 16777220 and self.settings[3] == False:
			self.check_answer(self.text.text())
			if self.settings[1] == True:
				self.many_new_characters()
			else:
				self.new_character()
			self.text.setText("")
		elif e.key() == 16777220:
			self.check_answer_timeattack(self.text.text())
			self.text.setText("")
		else:
			self.text.setText(text + e.text())

	def new_character(self):
		indices = generate_one(hiragana, self.settings[2])
		i = 0
		for entry in self.questions:
			if entry.text() != "":
				i += 1
			else:
				break
		if i > 9:
			return None
		else:
			if self.settings[0] == True:
				self.questions[i].setText(hiragana_labels[indices[0]][indices[1]])
				self.answers[i] = str(romaji[indices[0]][indices[1]])
			else:
				self.questions[i].setText(f"<font size=4>{romaji[indices[0]][indices[1]]}</font>")
				self.answers[i] = str(hiragana[indices[0]][indices[1]])
		return None

	def many_new_characters(self):
		multiple = np.random.randint(5, 16)
		string = ""
		for i in range(0, multiple):
			if i > 0 and i+1 < multiple:
				space = np.random.rand()
			else:
				space = 1
			character_index = generate_one(hiragana, self.settings[2])
			self.answers[0] = ""
			if self.settings[0] == True:
				if space < 0.4 and not string.endswith(" "):
					string += " "
					self.answers[0] += " "
				else:
					string += hiragana_labels[character_index[0]][character_index[1]]
					self.answers[0] += romaji[character_index[0]][character_index[1]]
			else:
				if space < 0.4 and not string.endswith(" "):
					string += " "
					self.answers[0] += " "
				else:
					string += f"<font size=4>{romaji[character_index[0]][character_index[1]]}</font>"
					self.answers[0] += hiragana[character_index[0]][character_index[1]]
		self.questions[0].setText(string)
		return None

	def check_answer(self, answer):
		if answer == "":
			return None
		if answer == self.answers[0]:
			self.result.setText(f"<font size=4><font color=#1CED1C>Correct! {self.questions[0].text()} = {self.answers[0]}.</font>")
			self.stats[0] += 1
			self.options[2].setText(f"Right: {self.stats[0]}")
		else:
			self.result.setText(f"<font size=4><font color=#880000>Incorrect. {self.questions[0].text()} = {self.answers[0]}.</font>")
			self.stats[1] += 1
			self.options[3].setText(f"Wrong: {self.stats[1]}")
		self.answers[0] = ""
		self.questions[0].setText("")
		return None

	def new_character_timeattack(self):
		indices = generate_one(hiragana, self.settings[2])
		i = 0
		for entry in self.questions:
			if entry.text() != "":
				i += 1
			else:
				break
		if i >= self.settings[5]:
			QTimer.singleShot(10, self.new_character_timeattack)
			return None
		else:
			if self.settings[0] == True:
				self.questions[i].setText(hiragana_labels[indices[0]][indices[1]])
				self.answers[i] = str(romaji[indices[0]][indices[1]])
			else:
				self.questions[i].setText(f"<font size=4>{romaji[indices[0]][indices[1]]}</font>")
				self.answers[i] = str(hiragana[indices[0]][indices[1]])
			self.decaying[i] = True
		QTimer.singleShot(1, lambda _=None, i=i, m=self.score[2] + round(0.5+self.score[2]/20)*10: self.decay_question(i, m))
		if self.settings[4] == True and self.score[1] > 0:
			QTimer.singleShot(self.score[2], self.new_character_timeattack)
		return None

	def decay_question(self, i, milliseconds):
		if self.settings[4] == False:
			for i in range(0, len(self.questions)):
				self.answers[i] = ""
				self.questions[i].setText("")
			return None
		elif milliseconds == 1:
			if self.decaying[i] == True:
				self.result.setText(f"<font size=4><font color=#880000>{self.questions[i].text()[20:]} = {self.answers[i]}.</font>")
				self.score[1] += -1
				self.options[3].setText(f"Lives: {self.score[1]}")
				if self.settings[0] == True:
					(i1, i2) = indices_by_character(self.answers[i], romaji)
					self.stats[2][i1][i2][2] += 1
				else:
					(i1, i2) = indices_by_character(self.answers[i], hiragana)
					self.stats[3][i1][i2][2] += 1
			if self.score[1] <= 0:
				self.result.setText(f"<font size=4><font color=#880000>You died!</font>")
				self.options_button(13)
			self.questions[i].setText("")
			self.answers[i] = ""
			self.decaying[i] == False
			return None
		elif self.decaying[i] == False and self.questions[i].text().startswith("<font color="):
			self.questions[i].setText("<font color=#00" + "{:02x}".format(255) + f"00>{self.questions[i].text()[20:]}")
			QTimer.singleShot(1, lambda: self.decay_question(i, min(milliseconds-1, 350)))
		elif self.decaying[i] == False:
			self.questions[i].setText("<font color=#00" + "{:02x}".format(255) + f"00>{self.questions[i].text()}")
			QTimer.singleShot(1, lambda: self.decay_question(i, min(milliseconds-1, 350)))
		elif self.questions[i].text().startswith("<font color="):
			self.questions[i].setText("<font color=#" + "{:02x}".format(round(0.5+max(min(-(255/2000)*milliseconds+255,255),0))) + f"0000>{self.questions[i].text()[20:]}")
			QTimer.singleShot(1, lambda: self.decay_question(i, milliseconds-1))
		else:
			self.questions[i].setText("<font color=#" + "{:02x}".format(round(0.5+max(min(-(255/2000)*milliseconds+255,255),0))) + f"0000>{self.questions[i].text()}")
			QTimer.singleShot(1, lambda: self.decay_question(i, milliseconds-1))
		return None

	def check_answer_timeattack(self, answer):
		self.result.setText("")
		if answer == "":
			return None
		for i in range(0, len(self.answers)):
			if answer == self.answers[i]:
				self.result.setText(f"<font size=4><font color=#1CED1C>Correct! {self.questions[i].text()[20:]} = {self.answers[i]}.</font>")
				self.score[0] += 1
				self.options[2].setText(f"Score: {self.score[0]}")
				self.decaying[i] = False
				if self.settings[0] == True:
					(i1, i2) = indices_by_character(answer, romaji)
					self.stats[2][i1][i2][1] += 1
					self.stats[2][i1][i2][2] += 1
				else:
					(i1, i2) = indices_by_character(answer, hiragana)
					self.stats[3][i1][i2][1] += 1
					self.stats[3][i1][i2][2] += 1
				break
		self.score[2] = round(0.5+max(2000*1.01**(-3*np.sqrt(self.score[0])), 200) + 100*(11-self.score[1]))
		return None


	def options_button(self, x):
		#print(x)
		#				   QPushButton("Start"),
		#				   QPushButton("Reset Score"),
		#				   QPushButton("End")]
		if x == 0: # Hiragana button
			self.settings[0] = True
			self.options_buttons[0].setFlat(True)
			self.options_buttons[1].setFlat(False)
			self.options_buttons[15].setEnabled(True)
		elif x == 1: # Romaji button
			self.settings[0] = False
			self.options_buttons[0].setFlat(False)
			self.options_buttons[1].setFlat(True)
			self.settings[6] = False
			for i in range(0, len(self.keys[1])): # Change button/label settings for the hiragana keyboard
				for j in range(0, len(self.keys[1][i])):
					self.keys[0][i][j].setEnabled(not self.settings[6])
					self.keys[1][i][j].setHidden(self.settings[6])
			self.options_buttons[15].setFlat(False)
			self.options_buttons[15].setEnabled(False)
		elif x == 2: # Single Characters button
			self.settings[1] = False
			self.options_buttons[3].setFlat(False)
			self.options_buttons[2].setFlat(True)
		elif x == 3: # Multiple Characters button
			self.settings[1] = True
			self.options_buttons[2].setFlat(False)
			self.options_buttons[3].setFlat(True)
			self.options_buttons[8].setFlat(False)
			self.options_buttons[11].setEnabled(False)
			self.options_buttons[13].setEnabled(False)
			self.settings[3] = False
		elif x == 4: # All Characters button
			self.settings[2] = 0
			self.options_buttons[5].setFlat(False)
			self.options_buttons[4].setFlat(True)
			self.options_buttons[6].setFlat(False)
			self.options_buttons[7].setFlat(False)
		elif x == 5: # No Digraphs button
			self.settings[2] = 1
			self.options_buttons[4].setFlat(False)
			self.options_buttons[5].setFlat(True)
			self.options_buttons[6].setFlat(False)
			self.options_buttons[7].setFlat(False)
		elif x == 6: # No Graphemes button
			self.settings[2] = 2
			self.options_buttons[4].setFlat(False)
			self.options_buttons[6].setFlat(True)
			self.options_buttons[5].setFlat(False)
			self.options_buttons[7].setFlat(False)
		elif x == 7: # Neither digraphs nor graphemes button
			self.settings[2] = 3
			self.options_buttons[4].setFlat(False)
			self.options_buttons[5].setFlat(False)
			self.options_buttons[6].setFlat(False)
			self.options_buttons[7].setFlat(True)
		elif x == 8: # Time Attack button
			self.settings[3] = not self.settings[3]
			if self.settings[3] == True:
				self.options_buttons[8].setFlat(True)
				self.settings[1] = False
				self.options_buttons[2].setFlat(True)
				self.options_buttons[3].setFlat(False)
				self.options_buttons[11].setEnabled(True)
				self.options_buttons[3].setEnabled(False)
				self.options_buttons[2].setEnabled(False)
				self.options[2].setText(f"Score: {self.score[0]}")
				self.options[3].setText(f"Lives: {self.score[1]}")
				self.options_buttons[14].setEnabled(True)
			else:
				self.options_buttons[11].setEnabled(False)
				self.options_buttons[13].setEnabled(False)
				self.options_buttons[8].setFlat(False)
				self.options_buttons[3].setEnabled(True)
				self.options_buttons[2].setEnabled(True)
				self.options_buttons[14].setEnabled(False)
				self.options[2].setText(f"Right: {self.stats[0]}")
				self.options[3].setText(f"Wrong: {self.stats[1]}")
		elif x == 9: # Up arrow button
			self.options_buttons[10].setEnabled(True)
			self.settings[5] = min(self.settings[5] + 1, 10)
			self.options[1].setText(f"Max Kana: {self.settings[5]}")
			if self.settings[5] == 10:
				self.options_buttons[9].setEnabled(False)
		elif x == 10: # Down arrow button
			self.options_buttons[9].setEnabled(True)
			self.settings[5] = max(1, self.settings[5]-1)
			self.options[1].setText(f"Max Kana: {self.settings[5]}")
			if self.settings[5] == 1:
				self.options_buttons[10].setEnabled(False)
		elif x == 11 and self.settings[3] == True: # Start button
			self.settings[4] = True
			self.score = [0, 10, 3100]
			self.options_buttons[11].setEnabled(False)
			self.options_buttons[13].setEnabled(True)
			QTimer.singleShot(500, self.new_character_timeattack)
			self.options[2].setText(f"Score: {self.score[0]}")
			self.options[3].setText(f"Lives: {self.score[1]}")
		elif x == 12: # Reset stats button
			self.stats = [0, 0, [], []]
			for i1 in range(0, len(hiragana)):
				for i2 in range(0, len(hiragana[i1])):
					self.stats[2].append([hiragana[i1][i2], 0])
					self.stats[3].append([romaji[i1][i2], 0])
			self.options[2].setText(f"Right: {self.stats[0]}")
			self.options[3].setText(f"Wrong: {self.stats[1]}")
		elif x == 13: # End button
			self.settings[4] = False
			self.options_buttons[13].setEnabled(False)
			if self.settings[3] == True:
				self.options_buttons[11].setEnabled(True)
			self.score = [0, 10, 3100]
			self.options[2].setText(f"Score: {self.score[0]}")
			self.options[3].setText(f"Lives: {self.score[1]}")
			self.decaying = [False for i in range(0,10)]
			if self.settings[0] == True:
				for entry in self.stats[2]:
					print(entry)
			else:
				for entry in self.stats[3]:
					print(entry)
		elif x == 14:
			os.system("clear")
			print("First entry: character, Second entry: correctly identified, Third entry: # of appearances (in time attack mode).")
			print("From Hiragana to Romaji")
			for entry in self.stats[2]:
				print(entry)
			print("\nFrom Romaji to Hiragana")
			for entry in self.stats[3]:
				print(entry)
		elif x == 15:
			if self.settings[0] == True:
				self.settings[6] = not self.settings[6]
			else:
				self.settings[6] == True
			for i in range(0, len(self.keys[1])):
				for j in range(0, len(self.keys[1][i])):
					self.keys[0][i][j].setEnabled(not self.settings[6])
					self.keys[1][i][j].setHidden(self.settings[6])
			self.options_buttons[15].setFlat(self.settings[6])
		if x != 11 and x != 9 and x != 10:
			self.settings[4] = False
			for entry in self.questions:
					entry.setText("")
			if self.settings[3] == False and self.settings[1] == False:
				self.new_character()
			elif self.settings[3] == False and self.settings[1] == True:
				#self.questions[0].						set the width of the label here
				self.many_new_characters()
		self.result.setText("")
		#print(self.settings)
		return None

App = QApplication(sys.argv)

accwindow = MainWindow()
accwindow.show()
accwindow.new_character()
sys.exit(App.exec_())
