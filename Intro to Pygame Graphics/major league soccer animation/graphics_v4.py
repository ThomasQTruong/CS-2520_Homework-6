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
    """Initializes data and starts creating graphics."""
    GraphicsData()
    cls.start_game()


  @classmethod
  def start_game(cls):
    """Creates interactive map.
    
    Keybinds can change the map environment.
    [D] - toggle day/night.
    [L] - toggle flood lights.
    """
    while not GraphicsData.done:
      # Event processing (React to key presses, mouse clicks, etc.)
      # for now, we'll just check to see if the X is clicked.
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          GraphicsData.done = True
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_l:
            GraphicsData.lights_on = not GraphicsData.lights_on
          elif event.key == pygame.K_d:
            GraphicsData.day = not GraphicsData.day

      # Adjust colors based on if light is on or not.
      if GraphicsData.lights_on:
        GraphicsData.light_color = GraphicsColors.YELLOW
      else:
        GraphicsData.light_color = GraphicsColors.SILVER

      # Adjust colors based on if it is day or night.
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

      # Drawing code (Describe the picture. It isn't actually drawn yet.)
      GraphicsData.screen.fill(GraphicsData.sky_color)
      GraphicsData.SEE_THROUGH.fill(GraphicsColors.ck)
      GraphicsData.SEE_THROUGH.set_colorkey(GraphicsColors.ck)

      # Draw stars if it is night time.
      if not GraphicsData.day:
        for star in GraphicsData.stars:
          pygame.draw.ellipse(GraphicsData.screen, GraphicsColors.WHITE, star)

      # Draw the playing field.
      GraphicsDrawer.draw_field()

      # Draw fence.
      GraphicsDrawer.draw_fence()

      # Draws sun/moon based on day/night.
      GraphicsDrawer.draw_sun_or_moon()

      # Change cloud positions for animation.
      GraphicsData.adjust_position_of_clouds()

      # Draw clouds.
      GraphicsDrawer.draw_all_clouds()

      # Draw out of bounds lines.
      GraphicsDrawer.draw_boundary_lines()

      # Draws the safety circle.
      GraphicsDrawer.draw_safety_circle()

      # Draws the 18 yard line goal box with an arc above it.
      GraphicsDrawer.draw_18_yard_box()

      # Draws the score board.
      GraphicsDrawer.draw_score_board()

      # Draws the frames of the goal.
      GraphicsDrawer.draw_goal_frame()

      # Draws the net for the goal.
      GraphicsDrawer.draw_goal_net()

      # Draws the 6 yard line goal box.
      GraphicsDrawer.draw_6_yard_box()

      # Draws the flood lights.
      GraphicsDrawer.draw_flood_light_1()
      GraphicsDrawer.draw_flood_light_2()

      # Draws the stands where people sit.
      GraphicsDrawer.draw_stands()

      # Draws the corner flags.
      GraphicsDrawer.draw_corner_flags()

      # Makes the game dark if it is night and the lights are not on.
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
