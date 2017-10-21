
import pygame as pg
import Coords

class Bird:
	def __init__(self, dispSurf, fpsClock, FPS, coords=None):
		self.dispSurf = dispSurf
		self.FPS = FPS
		self.fpsClock = fpsClock
		self.imagesPath = self.setImagePath()
		self.images = self.loadImages("objects/bird/", self.imagesPath)
		self.cur = 0
		self.prev_time_step = pg.time.get_ticks()
		self.cur_time_step = pg.time.get_ticks()
		self.time_diff = 40
		self.coords = coords
		self.g = -10.8
		self.v = 0
		self.divisor = 50

	def setImagePath(self):
		c = 1
		img = []
		while c < 15:
			img.append("bird_"+str(c)+".png")
			c+=1
		return img

	def loadImages(self, path, listOfImages):
		imgs = []
		for img in listOfImages:
			imgs.append(pg.transform.scale(pg.image.load(path+img), (48, 48)))
		return imgs

	def showAnimation(self):
		self.cur_time_step = pg.time.get_ticks()
		if self.cur_time_step - self.prev_time_step < self.time_diff*5:
			self.calNewCoords()
		if self.cur_time_step - self.prev_time_step < self.time_diff:
			self.dispSurf.blit(self.images[self.cur-1], (self.coords.x, self.coords.y))
			return
		self.prev_time_step = self.cur_time_step	
		if self.cur == len(self.images):
			self.cur = 0
		else:
			self.dispSurf.blit(self.images[self.cur], (self.coords.x, self.coords.y))
			self.cur += 1

	def calNewCoords(self):
		t = (self.cur_time_step - self.prev_time_step)/self.divisor
		#print("cur time {!s} && diff {!s}".format(t, self.v * t + 0.5 * self.g * (t**2)))
		self.coords.y = int(self.coords.y - (self.v * t + 0.5 * self.g * (t**2)))
		if self.v > 0:
			self.v = int(self.v + self.g * t)
		elif self.v < 0:
			self.v = 0

	def MakeJump(self):
		if self.v <= 0:
			self.v = 35

	def getCoords(self):
		return self.coords