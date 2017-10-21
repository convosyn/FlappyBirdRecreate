import pygame as pg
import Coords
class Draws:
	def __init__(self, dispSurf = None, typeface = "./fonts/PG_Roof Runners_active.ttf", string = "test", fontsize = 40, coords = Coords.Coords((int(640/2), 60)), color_left = pg.Color(128, 128, 128), use_center = False):
		self.dispSurf = dispSurf
		self.fontObj = pg.font.Font(typeface, fontsize)
		self.fontObj = self.fontObj.render(str(string), True, color_left)
		self.textSurf = self.fontObj.get_rect()
		if use_center == False:
			self.textSurf.top, self.textSurf.left = coords.y, coords.x
		else:
			self.textSurf.center = (coords.x, coords.y)

	def drawFont(self):
		self.dispSurf.blit(self.fontObj, self.textSurf) 
