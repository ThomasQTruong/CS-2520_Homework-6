"""Contains tools used for drawing major league soccer game maps."""

import pygame
import math
from graphics_colors import GraphicsColors
from graphics_data import GraphicsData

class GraphicsDrawer:
  """Contains tools used for drawing major league soccer game maps."""

  @staticmethod
  def draw_field():
    """Draws the soccer field with alternating colors."""
    pygame.draw.rect(GraphicsData.screen, GraphicsData.field_color,
                     [0, 180, 800 , 420])
    pygame.draw.rect(GraphicsData.screen, GraphicsData.stripe_color,
                     [0, 180, 800, 42])
    pygame.draw.rect(GraphicsData.screen, GraphicsData.stripe_color,
                     [0, 264, 800, 52])
    pygame.draw.rect(GraphicsData.screen, GraphicsData.stripe_color,
                     [0, 368, 800, 62])
    pygame.draw.rect(GraphicsData.screen, GraphicsData.stripe_color,
                     [0, 492, 800, 82])


  @staticmethod
  def draw_fence():
    """Draws a fence that surrounds the soccer field."""
    y = 170
    for x in range(5, 800, 30):
      pygame.draw.polygon(GraphicsData.screen, GraphicsColors.NIGHT_GRAY,
                          [[x + 2, y], [x + 2, y + 15], [x, y + 15], [x, y]])

    y = 170
    for x in range(5, 800, 3):
      pygame.draw.line(GraphicsData.screen, GraphicsColors.NIGHT_GRAY,
                       [x, y], [x, y + 15], 1)

    x = 0
    for y in range(170, 185, 4):
      pygame.draw.line(GraphicsData.screen, GraphicsColors.NIGHT_GRAY,
                       [x, y], [x + 800, y], 1)

    if GraphicsData.day:
      pygame.draw.ellipse(GraphicsData.screen, GraphicsColors.BRIGHT_YELLOW,
                          [520, 50, 40, 40])
    else:
      pygame.draw.ellipse(GraphicsData.screen, GraphicsColors.WHITE,
                          [520, 50, 40, 40])
      pygame.draw.ellipse(GraphicsData.screen, GraphicsData.sky_color,
                          [530, 45, 40, 40])


  @staticmethod
  def draw_boundary_lines():
    """Draws the lines that determine the boundary of the field."""
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [0, 580], [800, 580], 5)
    #left
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [0, 360], [140, 220], 5)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [140, 220], [660, 220], 3)
    #right
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [660, 220], [800, 360], 5)


  @staticmethod
  def draw_safety_circle():
    """Draws the safety circle on the field."""
    pygame.draw.ellipse(GraphicsData.screen, GraphicsColors.WHITE,
                        [240, 500, 320, 160], 5)


  @staticmethod
  def draw_18_yard_box():
    """Draws the 18 yard goal box with an arc above it."""
    #18 yard goal box
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [260, 220], [180, 300], 5)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [180, 300], [620, 300], 3)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [620, 300], [540, 220], 5)
    #arc above the box
    pygame.draw.arc(GraphicsData.screen, GraphicsColors.WHITE,
                    [330, 280, 140, 40], math.pi, 2 * math.pi, 5)


  @staticmethod
  def draw_score_board():
    """Draws the score board."""
    #score board pole
    pygame.draw.rect(GraphicsData.screen, GraphicsColors.GRAY,
                     [390, 120, 20, 70])

    #score board
    pygame.draw.rect(GraphicsData.screen, GraphicsColors.BLACK,
                     [300, 40, 200, 90])
    pygame.draw.rect(GraphicsData.screen, GraphicsColors.WHITE,
                     [302, 42, 198, 88], 2)


  @staticmethod
  def draw_goal():
    """Draws the goal."""
    pygame.draw.rect(GraphicsData.screen, GraphicsColors.WHITE,
    [320, 140, 160, 80], 5)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
    [340, 200], [460, 200], 3)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
    [320, 220], [340, 200], 3)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
    [480, 220], [460, 200], 3)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
    [320, 140], [340, 200], 3)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
    [480, 140], [460, 200], 3)


  @staticmethod
  def draw_6_yard_box():
    """Draws the 6 yard goal box."""
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
    [310, 220], [270, 270], 3)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
    [270, 270], [530, 270], 2)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
    [530, 270], [490, 220], 3)


  @staticmethod
  def draw_flood_light_1():
    """Draws the left flood light."""
    #light pole 1
    pygame.draw.rect(GraphicsData.screen, GraphicsColors.GRAY,
                     [150, 60, 20, 140])
    pygame.draw.ellipse(GraphicsData.screen, GraphicsColors.GRAY,
                        [150, 195, 20, 10])

    #lights
    pygame.draw.line(GraphicsData.screen, GraphicsColors.GRAY,
                     [110, 60], [210, 60], 2)
    pygame.draw.ellipse(GraphicsData.screen, GraphicsData.light_color,
                        [110, 40, 20, 20])
    pygame.draw.ellipse(GraphicsData.screen, GraphicsData.light_color,
                        [130, 40, 20, 20])
    pygame.draw.ellipse(GraphicsData.screen, GraphicsData.light_color,
                        [150, 40, 20, 20])
    pygame.draw.ellipse(GraphicsData.screen, GraphicsData.light_color,
                        [170, 40, 20, 20])
    pygame.draw.ellipse(GraphicsData.screen, GraphicsData.light_color,
                        [190, 40, 20, 20])
    pygame.draw.line(GraphicsData.screen, GraphicsColors.GRAY,
                     [110, 40], [210, 40], 2)
    pygame.draw.ellipse(GraphicsData.screen, GraphicsData.light_color,
                        [110, 20, 20, 20])
    pygame.draw.ellipse(GraphicsData.screen, GraphicsData.light_color,
                        [130, 20, 20, 20])
    pygame.draw.ellipse(GraphicsData.screen, GraphicsData.light_color,
                        [150, 20, 20, 20])
    pygame.draw.ellipse(GraphicsData.screen, GraphicsData.light_color,
                        [170, 20, 20, 20])
    pygame.draw.ellipse(GraphicsData.screen, GraphicsData.light_color,
                        [190, 20, 20, 20])
    pygame.draw.line(GraphicsData.screen, GraphicsColors.GRAY,
                    [110, 20], [210, 20], 2)


  @staticmethod
  def draw_flood_light_2():
    """Draws the right flood light."""
    #light pole 2
    pygame.draw.rect(GraphicsData.screen, GraphicsColors.GRAY,
                     [630, 60, 20, 140])
    pygame.draw.ellipse(GraphicsData.screen, GraphicsColors.GRAY,
                        [630, 195, 20, 10])

    #lights
    pygame.draw.line(GraphicsData.screen, GraphicsColors.GRAY,
                     [590, 60], [690, 60], 2)
    pygame.draw.ellipse(GraphicsData.screen, GraphicsData.light_color,
                        [590, 40, 20, 20])
    pygame.draw.ellipse(GraphicsData.screen, GraphicsData.light_color,
                        [610, 40, 20, 20])
    pygame.draw.ellipse(GraphicsData.screen, GraphicsData.light_color,
                        [630, 40, 20, 20])
    pygame.draw.ellipse(GraphicsData.screen, GraphicsData.light_color,
                        [650, 40, 20, 20])
    pygame.draw.ellipse(GraphicsData.screen, GraphicsData.light_color,
                        [670, 40, 20, 20])
    pygame.draw.line(GraphicsData.screen, GraphicsColors.GRAY,
                     [590, 40], [690, 40], 2)
    pygame.draw.ellipse(GraphicsData.screen, GraphicsData.light_color,
                        [590, 20, 20, 20])
    pygame.draw.ellipse(GraphicsData.screen, GraphicsData.light_color,
                        [610, 20, 20, 20])
    pygame.draw.ellipse(GraphicsData.screen, GraphicsData.light_color,
                        [630, 20, 20, 20])
    pygame.draw.ellipse(GraphicsData.screen, GraphicsData.light_color,
                        [650, 20, 20, 20])
    pygame.draw.ellipse(GraphicsData.screen, GraphicsData.light_color,
                        [670, 20, 20, 20])
    pygame.draw.line(GraphicsData.screen, GraphicsColors.GRAY,
                     [590, 20], [690, 20], 2)


  @staticmethod
  def draw_net():
    """Draws the net for the goal."""
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [325, 140], [341, 200], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [330, 140], [344, 200], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [335, 140], [347, 200], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [340, 140], [350, 200], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [345, 140], [353, 200], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [350, 140], [356, 200], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [355, 140], [359, 200], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [360, 140], [362, 200], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [364, 140], [365, 200], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [368, 140], [369, 200], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [372, 140], [373, 200], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [376, 140], [377, 200], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [380, 140], [380, 200], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [384, 140], [384, 200], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [388, 140], [388, 200], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [392, 140], [392, 200], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [396, 140], [396, 200], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [400, 140], [400, 200], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [404, 140], [404, 200], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [408, 140], [408, 200], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [412, 140], [412, 200], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [416, 140], [416, 200], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [420, 140], [420, 200], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [424, 140], [423, 200], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [428, 140], [427, 200], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [432, 140], [431, 200], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [436, 140], [435, 200], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [440, 140], [438, 200], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [445, 140], [441, 200], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [450, 140], [444, 200], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [455, 140], [447, 200], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [460, 140], [450, 200], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [465, 140], [453, 200], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [470, 140], [456, 200], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [475, 140], [459, 200], 1)

    #net part 2
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [320, 140], [324, 216], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [320, 140], [326, 214], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [320, 140], [328, 212], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [320, 140], [330, 210], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [320, 140], [332, 208], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [320, 140], [334, 206], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [320, 140], [336, 204], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [320, 140], [338, 202], 1)

    #net part 3
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [480, 140], [476, 216], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [480, 140], [474, 214], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [480, 140], [472, 212], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [480, 140], [470, 210], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [480, 140], [468, 208], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [480, 140], [466, 206], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [480, 140], [464, 204], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [480, 140], [462, 202], 1)

    #net part 4
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [324, 144], [476, 144], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [324, 148], [476, 148], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [324, 152], [476, 152], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [324, 156], [476, 156], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [324, 160], [476, 160], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [324, 164], [476, 164], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [324, 168], [476, 168], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [324, 172], [476, 172], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [324, 176], [476, 176], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [335, 180], [470, 180], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [335, 184], [465, 184], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [335, 188], [465, 188], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [335, 192], [465, 192], 1)
    pygame.draw.line(GraphicsData.screen, GraphicsColors.WHITE,
                     [335, 196], [465, 196], 1)


  @staticmethod
  def draw_stands():
    """Draws the stands where people sit."""
    #stands right
    pygame.draw.polygon(GraphicsData.screen, GraphicsColors.RED,
                        [[680, 220], [800, 340], [800, 290], [680, 180]])
    pygame.draw.polygon(GraphicsData.screen, GraphicsColors.WHITE,
                        [[680, 180], [800, 100], [800, 290]])

    #stands left
    pygame.draw.polygon(GraphicsData.screen, GraphicsColors.RED,
                        [[120, 220], [0, 340], [0, 290], [120, 180]])
    pygame.draw.polygon(GraphicsData.screen, GraphicsColors.WHITE,
                        [[120, 180], [0, 100], [0, 290]])
    #people


  @staticmethod
  def draw_corner_flags():
    """Draws the corner flags."""
    #corner flag right
    pygame.draw.line(GraphicsData.screen, GraphicsColors.BRIGHT_YELLOW,
                     [140, 220], [135, 190], 3)
    pygame.draw.polygon(GraphicsData.screen, GraphicsColors.RED,
                        [[132, 190], [125, 196], [135, 205]])

    #corner flag left
    pygame.draw.line(GraphicsData.screen, GraphicsColors.BRIGHT_YELLOW,
                     [660, 220], [665, 190], 3)
    pygame.draw.polygon(GraphicsData.screen, GraphicsColors.RED,
                        [[668, 190], [675, 196], [665, 205]])
