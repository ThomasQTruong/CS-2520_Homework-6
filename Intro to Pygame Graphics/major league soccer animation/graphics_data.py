"""Contains data and functions used for graphics creation."""

import pygame
import random
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

  # Set DARKNESS and SEE_THROUGH layers.
  DARKNESS = pygame.Surface(SIZE)
  DARKNESS.set_alpha(200)
  DARKNESS.fill((0, 0, 0))

  SEE_THROUGH = pygame.Surface((800, 180))
  SEE_THROUGH.set_alpha(150)
  SEE_THROUGH.fill((124, 118, 135))

  # Initially day; set color scheme for day.
  light_color = GraphicsColors.YELLOW
  sky_color = GraphicsColors.BLUE
  field_color = GraphicsColors.GREEN
  stripe_color = GraphicsColors.DAY_GREEN
  cloud_color = GraphicsColors.WHITE

  # Game loop
  done = False


  @classmethod
  def __init__(cls):
    """Initializes stars[] and clouds[]."""
    cls.generate_stars(200)
    cls.generate_clouds(20)


  @staticmethod
  def generate_stars(amount: int):
    """Generates a certain amount of stars.
    
    Stars are generated at random coordinates
    and stored into stars[] from GraphicsData.

    Args:
      amount: The amount of stars to create.
    """
    for _ in range(amount):
      random_x = random.randrange(0, 800)
      random_y = random.randrange(0, 200)
      random_r = random.randrange(1, 2)
      GraphicsData.stars.append([random_x, random_y, random_r, random_r])


  @staticmethod
  def generate_clouds(amount: int):
    """Generates a certain amount of clouds.
    
    Clouds are generated at random coordinates
    and stored into clouds[] from GraphicsData.

    Args:
      amount: The amount of clouds to create.
    """
    for _ in range(amount):
      random_x = random.randrange(-100, 1600)
      random_y = random.randrange(0, 150)
      GraphicsData.clouds.append([random_x, random_y])


  @staticmethod
  def adjust_position_of_clouds():
    """Changes every cloud's position.
    
    Makes every cloud move by 0.5 to the left.
    Randomly sets new position of x in the range [800-1600]
    and y in the range [0, 150] if it fully made its way left.
    """
    for cloud in GraphicsData.clouds:
      # Move left by 0.5
      cloud[0] -= 0.5

      # Reached the end (full left), generate new positions.
      if cloud[0] < -100:
        cloud[0] = random.randrange(800, 1600)
        cloud[1] = random.randrange(0, 150)
