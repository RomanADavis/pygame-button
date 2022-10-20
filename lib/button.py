import pygame

from lib.colors import WHITE, DARK_BLUE, RED_BROWN
from lib.setup import SCREEN

class Button():
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y
    self.width = 100
    self.height = 50
    self.set_rect()

    self.text_color = WHITE
    self.color = DARK_BLUE
    self.over_color = RED_BROWN

    self.font = pygame.font.SysFont("Arial", 20)
    self.text = self.font.render("QUIT", True, self.text_color)

  def set_rect(self):
    self.rect = [self.x, self.y, self.width, self.height]

  def center(self):
    self.x = SCREEN.get_width() // 2 - self.width // 2
    self.y = SCREEN.get_height() // 2 - self.height // 2
    self.set_rect()

  def draw(self):
    pygame.draw.rect(SCREEN, self.color, self.rect)
    SCREEN.blit(self.text, 
                (self.x + (self.width - self.text.get_width()) // 2,
                self.y + (self.height - self.text.get_height()) // 2)
                )