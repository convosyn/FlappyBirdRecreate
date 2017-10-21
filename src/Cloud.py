import pygame as pg
import Coords

class Cloud:
	def __init__(self, dispSurf, sizeOfScreen):
		self.dispSurf = dispSurf
		self.sizeOfScreen = sizeOfScreen
		self.cloudImage = pg.transform.scale(pg.image.load('objects/cloud/cloud.jpg'), (640, 480))
		self.cloud_r = self.cloudImage.get_rect()

	def drawCloud(self):
		for i in range(0, self.sizeOfScreen.x, self.cloud_r.width):
			for j in range(0, self.sizeOfScreen.y, self.cloud_r.height):
				self.dispSurf.blit(self.cloudImage, (i, j))
