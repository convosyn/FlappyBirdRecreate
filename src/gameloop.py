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

	def clear_data(self):
		self.score = 0
		self.bird = Bird.Bird(self.window, self.fpsClock, self.FPS, Coords.Coords((100, int(480/2))))
		self.curTime = self.prevTime = pg.time.get_ticks()
		self.time_diff = 3500
		self.grass = Grass.Grass(self.window, Coords.Coords((640, 480)))
		self.cloud = Cloud.Cloud(self.window, Coords.Coords((640, 480)))
		self.pipes = [Pipe.Pipe(self.window, Coords.Coords((640, 480)))]


	def run(self):
		self.startScreen()
		while True:
			self.clear_data()
			self.mainGame()
			self.gameOver()

	def mainGame(self):
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

	def startScreen(self):
		startCloud = pg.transform.scale(pg.image.load('objects/startscreen/cloud.jpg'), (640, 480))
		startbird = pg.transform.scale(pg.image.load("objects/startscreen/bird.png"), (64, 64))
		startPlayButton = pg.transform.scale(pg.image.load('objects/startscreen/play.png'),(128, 128))
		c = None
		startFlappyBird = TypeFaces.Draws(dispSurf = self.window, typeface="./fonts/CHLORINR.TTF", string="FLaPpY Wings", fontsize = 72, coords = Coords.Coords((int(640/2), int(480/5))), use_center = True, color_left=pg.Color(0, 120, 0))
		startCloudRect = startCloud.get_rect()
		startCloudRect.top = startCloudRect.left = 0
		startbirdRect = startbird.get_rect()
		startbirdRect.centerx = 60
		startbirdRect.centery = int(480/2)
		startPlayButtonRect = startPlayButton.get_rect()
		startPlayButtonRect.centerx = int(640/2)
		startPlayButtonRect.centery = int(480/2)
		mouseClicked = False
		while True:
			self.window.fill((0, 0, 0))
			self.window.blit(startCloud, startCloudRect)
			self.window.blit(startbird, startbirdRect)
			self.window.blit(startPlayButton, startPlayButtonRect)
			startFlappyBird.drawFont()
			self.checkForQuit()
			for event in pg.event.get():
				if event.type == pglcl.MOUSEBUTTONUP:
					c = Coords.Coords(event.pos)
					mouseClicked = True 
			if mouseClicked == True and startPlayButtonRect.colliderect(pg.Rect(c.x, c.y, startPlayButtonRect.width, startPlayButtonRect.height)) == True:
				return
			pg.display.update()
			self.fpsClock.tick(self.FPS)


	def gameOver(self):
		GameOverSurface = pg.Surface((640, 480))
		GameOverSurface = GameOverSurface.convert_alpha()
		GameOverSurface.fill((0, 0, 0, 50))
		gameOverGameOver = TypeFaces.Draws(dispSurf = self.window, typeface="./fonts/CHLORINR.TTF", string="Game Over", fontsize = 72, coords = Coords.Coords((int(640/2), int(480/2))), use_center = True, color_left=pg.Color(0, 120, 0)) 
		self.window.blit(GameOverSurface, (0, 0))
		gameOverGameOver.drawFont()
		pg.display.update()
		while True:
			self.checkForQuit()
			for event in pg.event.get():
				if event.type == pglcl.KEYUP:
					return



