#----Import system----
import tkinter as tk
from PIL import Image, ImageTk
from random import randint
from datetime import datetime

#----Import resources----

#----Typing speed----
class Typing(tk.Frame):

	#---about---
	def __init__(self, parent, App):
		self.app = App
		self.settings = App.settings

		#---Following config---
		super().__init__(parent)
		self.grid(column=0, row=0, sticky='nesw')
		parent.grid_rowconfigure(0, weight=1)
		parent.grid_columnconfigure(0, weight=1)

		self.main_screen()
		self.config_main_frame()

	def main_screen(self):
		self.main_frame = tk.Frame(self, bg='pink', width=self.settings.width)
		self.main_frame.grid(column=0, row=0, sticky='nesw')

		self.base_frame()
		self.create_background()

	def base_frame(self):
		self.base_frame = tk.Frame(self.main_frame, bg='blue', width=self.settings.width, height=self.settings.height)
		self.base_frame.grid(column=0, row=0, sticky='nesw')

		self.main_frame.grid_columnconfigure(0, weight=1)
		self.main_frame.grid_rowconfigure(0, weight=1)

	def create_background(self):
		image = Image.open(self.settings.typing_background)
		iW, iH = image.size
		ratio = iW/self.settings.width
		newSize = (int(iW/ratio), int(iH/ratio))
		image = image.resize(newSize)

		self.typing_background = ImageTk.PhotoImage(image)

		self.canvas = tk.Canvas(self.base_frame, width=self.settings.width, height=self.settings.height)
		self.canvas.pack(fill='both', expand=True)

		#---Set the image---
		self.canvas.create_image(0,0, image=self.typing_background, anchor='nw')

		self.create_title_and_button()
		self.create_sentence()
		self.create_entry_box()

	def create_title_and_button(self):
		self.canvas.create_text(490, 60, text='Typing Speed Test', font=('Times', 50, 'bold'), fill='goldenrod2')

		self.button_return_to_menu = tk.Button(self.base_frame, text='<-- Main menu', font=('Helvetica', 15), command=self.app.return_to_menu, bg="goldenrod1", fg='black')
		self.button_return_to_menu_window = self.canvas.create_window(10, 450, anchor='nw', window=self.button_return_to_menu)

	def create_sentence(self):
		#self.sentence_frame = tk.Frame(self.base_frame, width=self.settings.width//1.1, height=self.settings.height//5, bg='black')
		#self.sentence_frame_window = self.canvas.create_window(43, 150, anchor='nw', window=self.sentence_frame)

		self.sentence = self.app.sentences
		a = randint(0, len(self.sentence)-1)
		self.text = self.sentence[a]
		#print(self.text)
		
		self.text_label = self.canvas.create_text(465, 155, text=self.sentence[a], font=('Helvetica', 16), fill='white')

	def random_sentence(self):
		self.sentence = self.app.sentences
		a = randint(0, len(self.sentence) - 1)
		self.text = self.sentence[a]
		#print(self.text)

		#self.text_label = self.canvas.create_text(465, 155, text=self.text, font=('Helvetica', 16), fill='white')
		self.canvas.itemconfigure(self.text_label,text=self.text)

	def reset_timer(self, tab):
		self.finish_time = 0
		self.start_time = 0
		self.time_needed = 0
		self.canvas.itemconfigure(self.accuracy_label,text='')
		self.canvas.itemconfigure(self.word_per_minute_label,text='')
		self.canvas.itemconfigure(self.time_needed_label,text='')
		self.entry_sentence_box.delete(0, len(self.answer))
		self.random_sentence()

	def time_counter(self, enter):
		self.answer = self.entry_sentence.get()
		self.finish_time = datetime.now()
		self.accuracy = self.settings.accuracy
		time_needed = self.finish_time - self.start_time
		self.time_needed = time_needed.seconds
		if self.time_needed == 0:
			self.time_needed = 1

		Quest, Answer = len(self.text) - 1, len(self.answer)
		false = 0
		correct = 0
		for i in range(Quest):
			try:
				if self.text[i] == self.answer[i]:
					correct += 1
				
				else:
					false += 1
			except:
				pass

		if Answer > Quest:
			false += 1

		self.result = correct/(Quest)*100
		int(self.result)
		#print("%.2f %%"%result)
		#print(self.time_needed)
		self.print_result()

	def start_timer(self, key):
		self.answer = self.entry_sentence.get()
		if len(self.answer) == 1:
			self.start_time = datetime.now()
			#print(self.start_time)

	def create_entry_box(self):
		image = Image.open(self.settings.entry_background)
		iW, iH = image.size
		ratio = iW/self.settings.width*3
		newSize = (int(2*self.settings.width//3), int(iH/ratio))
		image = image.resize(newSize)
		image_w, image_h = image.size

		self.entry_background = ImageTk.PhotoImage(image)

		self.entry_background_canvas = self.canvas.create_image(160, 210, image=self.entry_background, anchor='nw')

		self.entry_sentence = tk.StringVar()
		self.entry_sentence_box = tk.Entry(self.base_frame, textvariable=self.entry_sentence,width=self.settings.width//15, bg='black', fg='goldenrod2', font=('Helvetica', 12, 'bold'))
		self.entry_sentence_box.bind("<Key>", self.start_timer)
		self.entry_sentence_box.bind("<Return>", self.time_counter)
		self.entry_sentence_box.bind("<Tab>", self.reset_timer)

		self.entry_sentence_box_window = self.canvas.create_window(480, 280, window=self.entry_sentence_box)

	def print_result(self):
		Answer = int(len(self.answer)/5*60/self.time_needed)
		time_needed = f'Time needed : {self.time_needed}'
		accuracy = 'Accuracy : %.2f'%self.result
		word_per_minute = f'Word per minute : {Answer}'
		self.time_needed_label = self.canvas.create_text(280, 400, text=time_needed, font=('Helvetica', 16), fill='white')
		self.accuracy_label = self.canvas.create_text(460, 400, text=accuracy, font=('Helvetica', 16), fill='white')
		self.word_per_minute_label = self.canvas.create_text(660, 400, text=word_per_minute, font=('Helvetica', 16), fill='white')

	def config_main_frame(self):
		self.grid_columnconfigure(0, weight=1) #1/3
		self.grid_rowconfigure(0, weight=1)