#----Import----
import tkinter as tk
from PIL import Image, ImageTk


#----How To Page----
class HowToPage(tk.Frame):

	def __init__(self, parent, App):
		self.app = App
		self.settings = App.settings

		#---Configuration---
		super().__init__(parent)
		self.grid(row=0, column=0, sticky="nsew")

		parent.grid_rowconfigure(0, weight=1)
		parent.grid_columnconfigure(0, weight=1)

		self.create_main_frame()

	def create_main_frame(self):
		self.main_frame = tk.Frame(self, bg='pink', width=self.settings.width)
		self.main_frame.grid(column=0, row=0, sticky='nesw')

		self.second_page_frame()
		self.create_howto_frame()

	def create_howto_frame(self):
		self.howto_frame = tk.Frame(self.main_frame, height=self.settings.height, width=self.settings.width, bg="pink")
		self.howto_frame.grid(column=0, row=0, sticky='nesw')

		self.main_frame.grid_columnconfigure(0, weight=1)
		self.main_frame.grid_rowconfigure(0, weight=1)

		self.create_background()
		self.create_button()

	def create_background(self):

		image = Image.open(self.settings.howto_background)
		iW, iH = image.size
		ratio = iW/self.settings.width
		newSize = (int(iW/ratio), int(iH/ratio))
		image = image.resize(newSize)
		
		#---Define Image---
		self.menu_background = ImageTk.PhotoImage(image)

		#---Create Canvas---
		self.howto_canvas = tk.Canvas(self.howto_frame, width=960, height=510)
		self.howto_canvas.pack(fill="both", expand=True)

		#---Insert Image to Canvas---
		self.howto_canvas.create_image(0, 0, image=self.menu_background, anchor="nw")

	def change_page(self):
		image = Image.open(self.settings.second_howto_background)
		iW, iH = image.size
		ratio = iW/self.settings.width
		newSize = (int(iW/ratio), int(iH/ratio))
		image = image.resize(newSize)
		
		#---Define Image---
		self.second_background = ImageTk.PhotoImage(image)

		#---Create Canvas---
		self.second_howto_canvas = tk.Canvas(self.second_frame, width=960, height=510)
		self.second_howto_canvas.pack(fill="both", expand=True)

		#---Insert Image to Canvas---
		self.second_howto_canvas.create_image(0, 0, image=self.second_background, anchor='nw')
	
	def second_page_frame(self):
		self.second_frame = tk.Frame(self.main_frame, width=self.settings.width, height=self.settings.height, bg='pink')
		self.second_frame.grid(column=0, row=0, sticky='nesw')

		self.main_frame.grid_columnconfigure(0, weight=1)
		self.main_frame.grid_rowconfigure(0, weight=1)

		self.change_page()
		self.return_page_1()

	def raise_page_2(self):
		self.second_frame.tkraise()

	def raise_page_1(self):
		self.howto_frame.tkraise()

	def return_page_1(self):
		self.button2 = tk.Button(self.second_frame, text='<-- Page 1', font=('Helvetica', 15), command=self.raise_page_1, bg="goldenrod1", fg='black')
		self.button2_win = self.second_howto_canvas.create_window(10, 450, anchor='nw', window=self.button2)

	def create_button(self):
		self.button1 = tk.Button(self.howto_frame, text='<-- Main menu', font=('Helvetica', 15), command=self.app.return_to_menu, bg="goldenrod1", fg='black')
		self.button1_win = self.howto_canvas.create_window(10, 450, anchor='nw', window=self.button1)

		self.button_how_to_play_page_2 = tk.Button(self.howto_frame, text='Next page -->', font=('Helvetica', 15), command=self.raise_page_2, bg="goldenrod1", fg='black')
		self.button_how_to_play_page_2 = self.howto_canvas.create_window(800, 450, anchor='nw', window=self.button_how_to_play_page_2)