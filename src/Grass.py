import pygame as pg
import Coords

class Grass:
	def __init__(self, dispSurf, sizeOfScreen):
		self.dispSurf = dispSurf
		self.sizeOfScreen = sizeOfScreen
		self.grassImage = pg.transform.scale(pg.image.load('objects/grass/grass.jpg'), (150, 60))
		self.grass_r = self.grassImage.get_rect()

	def drawGrass(self):
		for i in range(0, self.sizeOfScreen.x, self.grass_r.width):
			self.dispSurf.blit(self.grassImage, (i, self.sizeOfScreen.y-self.grass_r.height))

	def inrange(self, coords):
		#print("coords obtained >> {!s}".format((coords.x, coords.y, self.sizeOfScreen.y - self.grass_r.height)))
		if coords.y + 45 > self.sizeOfScreen.y - self.grass_r.height:
			return True
		else:
			return False
