import pygame

class Game():
  def __init__(self, width=600, height=600):
    pygame.init()
    self.screen = pygame.display.set_mode((width, height), 0, 32)
    pygame.display.set_caption("Hello Button")

  def run(self):
    from lib.button import Button
    game_over = False
    button = Button()
    button.center()
    while not game_over:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          game_over = True
      button.draw()
      pygame.display.update()
    
    self.quit()

  def quit(self):
    pygame.quit()

