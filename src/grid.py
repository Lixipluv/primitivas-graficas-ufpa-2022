import pygame
from math import floor, sqrt
from Algorithms.index import *
from sys import exit
from time import sleep

class Grid:
  def __init__(self, config: object):
    self.PIXELSIZE = config['pixels per rect']
    self.SIZE = config['size']
    self.shouldDrawGrid = config['grid']
    self.animate = config['animate']
    self.delay = config['delay']
    self.WHITE = (255, 255, 255)
    self.BLACK = (0, 0, 0)
    self.hLines = []
    self.vLines = []
    self.screen = pygame.display.set_mode((self.SIZE[0]*self.PIXELSIZE[0], self.SIZE[1]*self.PIXELSIZE[1]))
    pygame.display.set_caption('Grade')
    pygame.display.set_icon(pygame.image.load('src/assets/image.png'))

    for hLine in range(1, self.SIZE[0]):
      start = (hLine*self.PIXELSIZE[0], 0)
      end = (hLine*self.PIXELSIZE[0], self.PIXELSIZE[1]*self.SIZE[1])
      self.hLines.append((start, end))

    for vLine in range(1, self.SIZE[1]):
      start = (0, vLine*self.PIXELSIZE[1])
      end = (self.PIXELSIZE[0]*self.SIZE[0], vLine*self.PIXELSIZE[1])
      self.vLines.append((start, end))

  
  def drawPixel(self, position, color, animate=False):
    pos = (position[0]*self.PIXELSIZE[0], position[1]*self.PIXELSIZE[1])
    pygame.draw.rect(self.screen, color, pygame.Rect(pos, self.PIXELSIZE))
    if animate:
      self.drawGrid()
      pygame.display.update()
      sleep(self.delay)


  def drawGrid(self):
    if self.shouldDrawGrid:
      for hLine in self.hLines:
        start, end = hLine
        pygame.draw.line(self.screen, (80, 0, 0), start, end)

      for vLine in self.vLines:
        start, end = vLine
        pygame.draw.line(self.screen, (80, 0, 0), start, end)


  def launchPixelPainter(self):
    pygame.init()
    self.screen.fill(self.BLACK)

    running = True
    clock=pygame.time.Clock()

    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
          
        if event.type == pygame.MOUSEBUTTONUP:
          coords = (floor(event.pos[0]/self.PIXELSIZE[0]), floor(event.pos[1]/self.PIXELSIZE[1]))
          self.drawPixel(coords, self.WHITE, self.animate)

      clock.tick(60)
      self.drawGrid()
      pygame.display.update()
  
    pygame.quit()
    exit()

  def launchBresenham(self):
    selected = []
    running = True
    clock = pygame.time.Clock()

    self.screen.fill(self.BLACK)
    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
          pygame.display.quit()
          exit()

        if event.type == pygame.MOUSEBUTTONUP:
          if len(selected) == 0:
            self.screen.fill(self.BLACK)

          coords = (floor(event.pos[0]/self.PIXELSIZE[0]), floor(event.pos[1]/self.PIXELSIZE[1]))
          self.drawPixel(coords, self.WHITE)
          selected.append(coords)

          if len(selected) == 2:
            points = bres(selected[0], selected[1])
            start = selected[0]
            end = selected[1]
            selected = []
            self.screen.fill(self.BLACK)
            for point in points:
              self.drawPixel(point, self.WHITE, self.animate)

      clock.tick(60)
      self.drawGrid()
      pygame.display.update()  
  
    pygame.display.quit()
    exit()

  
  def launchSquares(self):
    selected = []
    running = True
    clock = pygame.time.Clock()

    self.screen.fill(self.BLACK)
    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
          pygame.display.quit()
          exit()

        if event.type == pygame.MOUSEBUTTONUP:
          if len(selected) == 0:
            self.screen.fill(self.BLACK)

          coords = (floor(event.pos[0]/self.PIXELSIZE[0]), floor(event.pos[1]/self.PIXELSIZE[1]))
          self.drawPixel(coords, self.WHITE)
          selected.append(coords)

          if len(selected) == 2:
            x1, y1 = selected[0]
            x2, y2 = selected[1]

            edges = [
              bres((x1, y1), (x2, y1)),
              bres((x2, y1), (x2, y2)),
              bres((x2, y2), (x1, y2)),
              bres((x1, y2), (x1, y1)),
            ]

            selected = []
            self.screen.fill(self.BLACK)
            for edge in edges:
              for point in edge:
                self.drawPixel(point, self.WHITE, self.animate)

      clock.tick(60)
      self.drawGrid()
      pygame.display.update()  
  
    pygame.display.quit()
    exit()

  
  def launchTriangles(self):
    selected = []
    running = True
    clock = pygame.time.Clock()

    self.screen.fill(self.BLACK)
    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
          pygame.display.quit()
          exit()

        if event.type == pygame.MOUSEBUTTONUP:
          if len(selected) == 0:
            self.screen.fill(self.BLACK)

          coords = (floor(event.pos[0]/self.PIXELSIZE[0]), floor(event.pos[1]/self.PIXELSIZE[1]))
          self.drawPixel(coords, self.WHITE)
          selected.append(coords)

          if len(selected) == 3:
            x1, y1 = selected[0]
            x2, y2 = selected[1]
            x3, y3 = selected[2]

            edges = [
              bres((x1, y1), (x2, y2)),
              bres((x2, y2), (x3, y3)),
              bres((x3, y3), (x1, y1))
            ]

            selected = []
            self.screen.fill(self.BLACK)
            for edge in edges:
              for point in edge:
                self.drawPixel(point, self.WHITE, self.animate)

      clock.tick(60)
      self.drawGrid()
      pygame.display.update()  
  
    pygame.display.quit()
    exit()


  def launchCircles(self):
    selected = []
    running = True
    clock = pygame.time.Clock()

    self.screen.fill(self.BLACK)
    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False

        if event.type == pygame.MOUSEBUTTONUP:
          if len(selected) == 0:
            self.screen.fill(self.BLACK)

          coords = (floor(event.pos[0]/self.PIXELSIZE[0]), floor(event.pos[1]/self.PIXELSIZE[1]))
          self.drawPixel(coords, self.WHITE)
          selected.append(coords)

          if len(selected) == 2:
            center = selected[0]
            x1, y1 = selected[0]
            x2, y2 = selected[1]

            radius = round(sqrt(((x2 - x1) ** 2) + (y2 - y1) ** 2))

            octants = circle(center, radius)

            selected = []
            self.screen.fill(self.BLACK)
            for octant in octants:
              for point in octant:
                self.drawPixel(point, self.WHITE, self.animate)

      clock.tick(60)
      self.drawGrid()
      pygame.display.update()  

    pygame.display.quit()
    exit()
  
  def launchEllipsis(self):
    selected = []
    running = True
    clock = pygame.time.Clock()
    oscilating = [30, 30, 30]
    increment = True
    mousePos = []

    self.screen.fill(self.BLACK)
    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
          pygame.display.quit()
          exit()

        if event.type == pygame.MOUSEMOTION:
          mousePos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
          if len(selected) == 0:
            self.screen.fill(self.BLACK)

          coords = (floor(event.pos[0]/self.PIXELSIZE[0]), floor(event.pos[1]/self.PIXELSIZE[1]))
          self.drawPixel(coords, self.WHITE)
          selected.append(coords)

          if len(selected) == 2:
            x1, y1 = selected[0]
            x2, y2 = selected[1]

            radii = (abs(x2-x1), abs(y2-y1))
            regions = ellipsis(radii, (x1, y1))

            selected = []
            self.screen.fill(self.BLACK)
            for region in regions:
              for point in region:
                self.drawPixel(point, self.WHITE, self.animate)

      if len(selected) == 1:
        coords = (floor(mousePos[0]/self.PIXELSIZE[0]), floor(mousePos[1]/self.PIXELSIZE[1]))

        x1, y1 = coords
        x2, y2 = selected[0]

        edges = []
        if x1 != x2 and y1 != y2:
          edges = [
            bres((x1, y1), (x2, y1)),
            bres((x2, y1), (x2, y2)),
            bres((x2, y2), (x1, y2)),
            bres((x1, y2), (x1, y1)),
          ]

        self.screen.fill(self.BLACK)
        self.drawPixel(selected[0], self.WHITE)
        for edge in edges:
          for point in edge:
            self.drawPixel(point, tuple(oscilating))


      clock.tick(60)
      self.drawGrid()
      pygame.display.update()

      if increment:
        oscilating[0] += 1
        oscilating[1] += 1
        oscilating[2] += 1

      else:
        oscilating[0] -= 1
        oscilating[1] -= 1
        oscilating[2] -= 1

      if oscilating[0] == 100:
        increment = False
      elif oscilating[0] == 30:
        increment = True
      
  
    pygame.display.quit()
    exit()
