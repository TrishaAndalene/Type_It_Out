#----Settings configuration---
class Settings:

	def __init__(self):

		#---Title-----
		self.title = "9th Last Semester"

		#---Geometry---
		base = 60
		self.width = 16*base
		self.height = int(8.5*base)
		self.screen = f"{self.width}x{self.height}+500+500"

		#---Image Path---
		self.window_icon = "image/tomioka rain.ico"
		self.menu_background = "image/menu_gold.png"
		self.typing_background = "image/typing_background_black.png"
		self.entry_background = "image/latar_entry.jpg"
		self.howto_background = "image/howtoplay.png"
		self.second_howto_background = 'image/howtoplay_2.png'
		self.credit_background = 'image/credits.png'

		#---Current status---
		self.accuracy = 0 