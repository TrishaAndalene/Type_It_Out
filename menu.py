#----Import system----
import tkinter as tk
from os import system
import pygame

#----Import resources----
from settings.settings import Settings
from pages.front_page import FrontPage
from pages.typing_speed import Typing
from pages.sentence import Sentence
from pages.howto_page import HowToPage
from pages.credit import Credit

#----Screen----
class Screen(tk.Tk):

	def __init__(self, App):
		self.app = App
		self.settings = App.settings
		self.sentence_library = Sentence()
		self.sentences = self.sentence_library.sentences

		#---About screen----
		super().__init__()
		self.title(self.settings.title)
		#self.iconbitmap(self.settings.window_icon)
		self.geometry(self.settings.screen)
		self.resizable(False, False)

		#---Create container---
		self.create_container()

		self.pages = {}
		self.create_credit_page()
		self.create_game_page()
		self.create_howto_page()
		self.create_pages()

	def create_container(self):
		self.container = tk.Frame(bg="white")
		self.container.pack(side='top', fill='both', expand=True)

	def create_pages(self):
		self.pages['front_page'] = FrontPage(self.container, self)

	def create_game_page(self):
		self.pages['typing_speed'] = Typing(self.container, self)

	def create_howto_page(self):
		self.pages['howto_page'] = HowToPage(self.container,self)

	def create_credit_page(self):
		self.pages['credit'] = Credit(self.container, self)

	def return_to_menu(self):
		self.pages['front_page'].tkraise()

	def return_to_typer(self):
		self.pages['typing_speed'].tkraise()
		self.pages['typing_speed'].random_sentence()

	def return_to_howto(self):
		self.pages['howto_page'].tkraise()

	def return_to_credit(self):
		self.pages['credit'].tkraise()

	def exit(self):
		exit()

#----Engine----
class Engine:

	def __init__(self):

		#---Configuration---
		self.settings = Settings()

		self.base = Screen(self)

	def start_music(self):
		pygame.mixer.init()
		pygame.mixer.music.load("image/background_music.mp3")
		pygame.mixer.music.set_volume(0.05)
		pygame.mixer.music.play(-1, 0.0)

	def run(self):
		system('cls')
		print("[!] The game will not be saved")
		self.start_music()
		self.base.mainloop()

#----Trigger----
if __name__ == '__main__':
	Project = Engine()
	Project.run()