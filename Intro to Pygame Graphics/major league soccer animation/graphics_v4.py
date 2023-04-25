"""Displays graphics for a major league soccer game.

Utilizes Graphics_Drawer.py to draw the graphics
for a major league soccer game animation.

Displays the major league soccer game map with
keybinds that change the map environment.
[D] - toggle day/night.
[L] - toggle flood lights.
"""

# Imports
import pygame
import random
from graphics_colors import GraphicsColors
from graphics_drawer import GraphicsDrawer
from graphics_data import GraphicsData

class GraphicsV4:
  """Displays graphics for a major league soccer game.

  Utilizes Graphics_Drawer.py to draw the graphics
  for a major league soccer game animation.

  Displays the major league soccer game map with
  keybinds that change the map environment.
  [D] - toggle day/night.
  [L] - toggle flood lights.
  """

  @classmethod
  def __init__(cls):
    """Initializes stars[] and clouds[] and create graphics."""
    cls.generate_stars(200)
    cls.generate_clouds(20)
    cls.start_game()

  @classmethod
  def generate_stars(cls, amount: int):
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

  @classmethod
  def generate_clouds(cls, amount: int):
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

  @classmethod
  def draw_cloud(cls, x_position: int, y_position: int):
    """Draws a cloud at a certain position.
    
    Args:
      x_position: The X position to draw the cloud.
      y_position: The Y position to draw the cloud.
    """
    pygame.draw.ellipse(GraphicsData.SEE_THROUGH, GraphicsData.cloud_color,
                        [x_position, y_position + 8, 10, 10])
    pygame.draw.ellipse(GraphicsData.SEE_THROUGH, GraphicsData.cloud_color,
                        [x_position + 6, y_position + 4, 8, 8])
    pygame.draw.ellipse(GraphicsData.SEE_THROUGH, GraphicsData.cloud_color,
                        [x_position + 10, y_position, 16, 16])
    pygame.draw.ellipse(GraphicsData.SEE_THROUGH, GraphicsData.cloud_color,
                        [x_position + 20, y_position + 8, 10, 10])
    pygame.draw.rect(GraphicsData.SEE_THROUGH, GraphicsData.cloud_color,
                     [x_position + 6, y_position + 8, 18, 10])

  @classmethod
  def start_game(cls):
    """Creates interactive map.
    
    Keybinds can change the map environment.
    [D] - toggle day/night.
    [L] - toggle flood lights.
    """
    while not GraphicsData.done:
      # Event processing (React to key presses, mouse clicks, etc.)
      # for now, we'll just check to see if the X is clicked
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          GraphicsData.done = True
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_l:
            GraphicsData.lights_on = not GraphicsData.lights_on
          elif event.key == pygame.K_d:
            GraphicsData.day = not GraphicsData.day

      # Game logic (Check for collisions, update points, etc.)
      # leave this section alone for now
      if GraphicsData.lights_on:
        GraphicsData.light_color = GraphicsColors.YELLOW
      else:
        GraphicsData.light_color = GraphicsColors.SILVER

      if GraphicsData.day:
        GraphicsData.sky_color = GraphicsColors.BLUE
        GraphicsData.field_color = GraphicsColors.GREEN
        GraphicsData.stripe_color = GraphicsColors.DAY_GREEN
        GraphicsData.cloud_color = GraphicsColors.WHITE
      else:
        GraphicsData.sky_color = GraphicsColors.DARK_BLUE
        GraphicsData.field_color = GraphicsColors.DARK_GREEN
        GraphicsData.stripe_color = GraphicsColors.NIGHT_GREEN
        GraphicsData.cloud_color = GraphicsColors.NIGHT_GRAY

      for c in GraphicsData.clouds:
        c[0] -= 0.5

        if c[0] < -100:
          c[0] = random.randrange(800, 1600)
          c[1] = random.randrange(0, 150)

      # Drawing code (Describe the picture. It isn't actually drawn yet.)
      GraphicsData.screen.fill(GraphicsData.sky_color)
      GraphicsData.SEE_THROUGH.fill(GraphicsColors.ck)
      GraphicsData.SEE_THROUGH.set_colorkey(GraphicsColors.ck)

      if not GraphicsData.day:
        #stars
        for s in GraphicsData.stars:
          pygame.draw.ellipse(GraphicsData.screen, GraphicsColors.WHITE, s)

      #field
      GraphicsDrawer.draw_field()

      #fence
      GraphicsDrawer.draw_fence()

      for c in GraphicsData.clouds:
        cls.draw_cloud(c[0], c[1])
      GraphicsData.screen.blit(GraphicsData.SEE_THROUGH, (0, 0))

      #out of bounds lines
      GraphicsDrawer.draw_boundary_lines()

      #safety circle
      GraphicsDrawer.draw_safety_circle()

      #18 yard line goal box with arc above it
      GraphicsDrawer.draw_18_yard_box()

      GraphicsDrawer.draw_score_board()

      #goal
      GraphicsDrawer.draw_goal()

      #6 yard line goal box
      GraphicsDrawer.draw_6_yard_box()

      #flood lights
      GraphicsDrawer.draw_flood_light_1()
      GraphicsDrawer.draw_flood_light_2()

      #net
      GraphicsDrawer.draw_net()

      #stands
      GraphicsDrawer.draw_stands()

      #corner flags
      GraphicsDrawer.draw_corner_flags()

      # DARKNESS
      if not GraphicsData.day and not GraphicsData.lights_on:
        GraphicsData.screen.blit(GraphicsData.DARKNESS, (0, 0))

      #pygame.draw.polygon(screen, BLACK,
      #                    [[200, 200], [50,400], [600, 500]], 10)

      # Angles for arcs are measured in radians (a pre-cal topic)
      #pygame.draw.arc(screen, ORANGE, [100, 100, 100, 100], 0, math.pi/2, 1)
      #pygame.draw.arc(screen, BLACK, [100, 100, 100, 100], 0, math.pi/2, 50)


      # Update screen (Actually draw the picture in the window.)
      pygame.display.flip()


      # Limit refresh rate of game loop
      GraphicsData.clock.tick(GraphicsData.refresh_rate)


    # Close window and quit
    pygame.quit()


if __name__ == "__main__":
  # Initialize game engine
  pygame.init()

  # Create graphics.
  GraphicsV4()
