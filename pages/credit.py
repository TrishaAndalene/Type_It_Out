#----Import system----
import tkinter as tk
from PIL import Image, ImageTk

#----Front Page----
class Credit(tk.Frame):

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

		self.create_credit_frame()

	def create_credit_frame(self):
		self.credit_frame = tk.Frame(self.main_frame, height=self.settings.height, width=self.settings.width, bg="pink")
		self.credit_frame.grid(column=0, row=0, sticky='nesw')

		self.main_frame.grid_columnconfigure(0, weight=1)
		self.main_frame.grid_rowconfigure(0, weight=1)

		self.create_background()
		self.create_button()

	def create_background(self):
		image = Image.open(self.settings.credit_background)
		iW, iH = image.size
		ratio = iW/self.settings.width
		newSize = (int(iW/ratio), int(iH/ratio))
		image = image.resize(newSize)
		
		#---Define Image---
		self.credit_background = ImageTk.PhotoImage(image)

		#---Create Canvas---
		self.credit_canvas = tk.Canvas(self.credit_frame, width=960, height=510)
		self.credit_canvas.pack(fill="both", expand=True)

		#---Insert Image to Canvas---
		self.credit_canvas.create_image(0, 0, image=self.credit_background, anchor='nw')

	def create_button(self):
		self.button1 = tk.Button(self.credit_frame, text='<-- Main menu', font=('Helvetica', 15), command=self.app.return_to_menu, bg='#17dbd9', fg='white')
		self.button1_win = self.credit_canvas.create_window(10, 450, anchor='nw', window=self.button1)