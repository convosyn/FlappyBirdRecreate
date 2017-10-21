import pygame as pg, pygame.locals as pglcl
import sys
import math
import Bird
import Coords
import Grass
import Cloud
import Pipe
import TypeFaces
class MainGameLoop:
	def __init__(self):
		pg.init()
		self.score = 0
		self.runGame = True
		self.game_screen()
		self.bird = Bird.Bird(self.window, self.fpsClock, self.FPS, Coords.Coords((100, int(480/2))))
		self.curTime = self.prevTime = pg.time.get_ticks()
		self.time_diff = 3500
		self.grass = Grass.Grass(self.window, Coords.Coords((640, 480)))
		self.cloud = Cloud.Cloud(self.window, Coords.Coords((640, 480)))
		self.pipes = [Pipe.Pipe(self.window, Coords.Coords((640, 480)))]

	def game_screen(self, size = (640, 480)):
		self.window = pg.display.set_mode(size)
		pg.display.set_caption("FLaPpY Wings")
		self.FPS = 60
		self.fpsClock = pg.time.Clock() 

	def checkForQuit(self):
		for event in pg.event.get(pglcl.QUIT):
			self.terminate()
		for event in pg.event.get(pglcl.KEYUP):
			if event.key == pglcl.K_ESCAPE:
				self.terminate()
			pg.event.post(event)

	def terminate(self):
		pg.quit()
		sys.exit()

	def run(self):
		self.runGame = True
		while self.runGame == True:
			if len(self.pipes) > 0 and self.pipes[0].visible == False:
				del self.pipes[0]
			for i in self.pipes:
				if i.inrange(self.bird.getCoords()) == True:
					return
			for i in self.pipes:
				if i.passed_pipe(self.bird.getCoords()) == True:
					self.score+=1
					break
			self.window.fill((0, 0, 0))
			self.checkForQuit()
			for event in pg.event.get():
				if event.type == pglcl.KEYDOWN and event.key == pglcl.K_UP:
					self.bird.MakeJump()
			self.curTime = pg.time.get_ticks()
			if self.curTime - self.prevTime > self.time_diff:
				self.pipes.append(Pipe.Pipe(self.window, Coords.Coords((640, 480))))
				self.prevTime = self.curTime
			self.cloud.drawCloud()
			self.grass.drawGrass()
			for i in self.pipes:
				i.drawPipe()
			TypeFaces.Draws(dispSurf = self.window, string = "{!s}".format(self.score), use_center = True).drawFont()
			self.bird.showAnimation()
			if self.grass.inrange(self.bird.getCoords()) or self.checkOutOfFrame(self.bird.getCoords()):
				break
			pg.display.update()
			self.fpsClock.tick(self.FPS)

	def checkOutOfFrame(self, coords):
		if coords.x < 0 or coords.x > 640 or coords.y < 0 or coords.y > 480:
			return True
		else:
		 return False

