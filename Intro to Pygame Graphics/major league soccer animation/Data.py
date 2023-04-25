import pygame
from Color import Color

class Data:
  # Window
  SIZE = (800, 600)
  TITLE = "Major League Soccer"
  screen = pygame.display.set_mode(SIZE)
  pygame.display.set_caption(TITLE)

  # Config
  lights_on = True
  day = True

  # Data
  stars = []
  clouds = []

  # Timer
  clock = pygame.time.Clock()
  refresh_rate = 60

  DARKNESS = pygame.Surface(SIZE)
  DARKNESS.set_alpha(200)
  DARKNESS.fill((0, 0, 0))

  SEE_THROUGH = pygame.Surface((800, 180))
  SEE_THROUGH.set_alpha(150)
  SEE_THROUGH.fill((124, 118, 135))

  # Initially day
  light_color = Color.YELLOW
  sky_color = Color.BLUE
  field_color = Color.GREEN
  stripe_color = Color.DAY_GREEN
  cloud_color = Color.WHITE

  # Game loop
  done = False