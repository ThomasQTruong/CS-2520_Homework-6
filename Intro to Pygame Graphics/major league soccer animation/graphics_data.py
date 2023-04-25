"""Contains data used for graphics creation."""

import pygame
from graphics_colors import GraphicsColors

class GraphicsData:
  """Contains data used for graphics creation."""
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
  light_color = GraphicsColors.YELLOW
  sky_color = GraphicsColors.BLUE
  field_color = GraphicsColors.GREEN
  stripe_color = GraphicsColors.DAY_GREEN
  cloud_color = GraphicsColors.WHITE

  # Game loop
  done = False
