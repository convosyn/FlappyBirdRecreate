import pygame as pg
import random

class Pipe:
	def __init__(self, dispSurf, screenSize):
		self.total_height = screenSize.y - 60
		self.imagePipe = pg.image.load('objects/pipe/pipe_upper.png')
		self.gap = 120
		self.coords = int((self.total_height-2*10-self.gap) * random.random())
		self.imagePipe1 = pg.transform.scale(self.imagePipe, (80, self.coords+8))
		self.imagePipe2 = pg.transform.rotate(pg.transform.scale(self.imagePipe, (80, self.total_height - 2 * 10 + 8 - self.gap - self.coords)), 180)
		self.left = screenSize.x-10
		self.visible = True
		self.dispSurf = dispSurf
		self.time_diff = 10
		self.prevTime = self.curTime = pg.time.get_ticks()
		self.rect1 = pg.Rect(self.imagePipe1.get_rect())
		self.rect1.bottom = self.total_height
		self.rect1.left = self.left
		self.rect2 = pg.Rect(self.imagePipe2.get_rect())
		self.rect2.top = 0
		self.passed = False
	
	def increment(self):
		self.curTime = pg.time.get_ticks()
		if self.curTime - self.prevTime < self.time_diff:
			return
		self.prevTime = self.curTime
		self.left -= 1
		if self.left + 150 < 0:
			self.visible = False

	def inrange(self, coords):
		rectc = pg.Rect((coords.x+10, coords.y+10), (20, 20))
		if rectc.collidelist([self.rect1, self.rect2]) != -1:
			return True
		else:
			return False

	def passed_pipe(self, coords):
		rectc = pg.Rect((coords.x+10, coords.y+10), (30, 20))
		if self.passed == False and rectc.x >= self.rect1.left and rectc.x <= self.rect1.right:
			self.passed = True
			return True
		else:
			return False


	def drawPipe(self):
		self.increment()
		self.rect1 = pg.Rect(self.imagePipe1.get_rect())
		self.rect1.bottom = self.total_height
		self.rect1.left = self.left
		self.rect2 = pg.Rect(self.imagePipe2.get_rect())
		self.rect2.top = 0
		self.rect2.left = self.left
		self.dispSurf.blit(self.imagePipe1, self.rect1)
		self.dispSurf.blit(self.imagePipe2, self.rect2)