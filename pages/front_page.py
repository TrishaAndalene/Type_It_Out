#----Import system----
import tkinter as tk
from PIL import Image, ImageTk



#----Front Page----
class FrontPage(tk.Frame):

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

		self.create_front_frame()
		self.create_background()
		self.create_title_text()
		self.create_button()

	def create_front_frame(self):
		self.front_frame = tk.Frame(self.main_frame, height=self.settings.height, width=self.settings.width, bg="pink")
		self.front_frame.grid(column=0, row=0, sticky='nesw')

		self.main_frame.grid_columnconfigure(0, weight=1)
		self.main_frame.grid_rowconfigure(0, weight=1)

	def create_background(self):

		image = Image.open(self.settings.menu_background)
		iW, iH = image.size
		ratio = iW/self.settings.width
		newSize = (int(iW/ratio), int(iH/ratio))
		image = image.resize(newSize)
		
		#---Define Image---
		self.menu_background = ImageTk.PhotoImage(image)

		#---Create Canvas---
		self.front_canvas = tk.Canvas(self.front_frame, width=960, height=510)
		self.front_canvas.pack(fill="both", expand=True)

		#---Insert Image to Canvas---
		self.front_canvas.create_image(0, 0, image=self.menu_background, anchor="nw")

	def create_title_text(self):
		self.front_canvas.create_text(480, 100, text="Type It Out", font=("Times", 60), fill="goldenrod1")

	def create_button(self):
		button1 = tk.Button(self.front_frame, text="Start", font=("Helvetica", 20), bg="goldenrod1", fg="black", command=self.app.return_to_typer, padx=97)
		button2 = tk.Button(self.front_frame, text="How To Play", font=("Helvetica", 20), bg="goldenrod1", fg="black", command=self.app.return_to_howto, padx=50)
		button3 = tk.Button(self.front_frame, text=" Credit ", font=("Helvetica", 20), bg="goldenrod1", fg="black", command=self.app.return_to_credit, padx=82)
		button4 = tk.Button(self.front_frame, text="Exit", font=("Helvetica", 20), bg="goldenrod1", fg="black", command=self.app.exit, padx=104)

		button1_win = self.front_canvas.create_window(360, 200, anchor="nw", window=button1)
		button2_win = self.front_canvas.create_window(360, 260, anchor="nw", window=button2)
		button3_win = self.front_canvas.create_window(360, 320, anchor="nw", window=button3)
		button4_win = self.front_canvas.create_window(360, 380, anchor="nw", window=button4)