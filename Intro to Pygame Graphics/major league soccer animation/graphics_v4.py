"""Creation of graphics for a major league soccer game.

Draws the graphics for a major league soccer game animation.
"""

# Imports
import pygame
import random
from Color import Color
from Graphics_Drawer import Graphics_Drawer
from Data import Data


# Initialize game engine
pygame.init()

class graphics_v4:
  def __init__(self):
    self.get_stars(200)
    self.get_clouds(20)
    self.start_game()

  def get_stars(self, amount: int):
    for _ in range(amount):
      random_x = random.randrange(0, 800)
      random_y = random.randrange(0, 200)
      random_r = random.randrange(1, 2)
      Data.stars.append([random_x, random_y, random_r, random_r])

  def get_clouds(self, amount: int):
    for _ in range(amount):
      random_x = random.randrange(-100, 1600)
      random_y = random.randrange(0, 150)
      Data.clouds.append([random_x, random_y])

  def draw_cloud(self, x_position: int, y_position: int):
    pygame.draw.ellipse(Data.SEE_THROUGH, Data.cloud_color,
                        [x_position, y_position + 8, 10, 10])
    pygame.draw.ellipse(Data.SEE_THROUGH, Data.cloud_color,
                        [x_position + 6, y_position + 4, 8, 8])
    pygame.draw.ellipse(Data.SEE_THROUGH, Data.cloud_color,
                        [x_position + 10, y_position, 16, 16])
    pygame.draw.ellipse(Data.SEE_THROUGH, Data.cloud_color,
                        [x_position + 20, y_position + 8, 10, 10])
    pygame.draw.rect(Data.SEE_THROUGH, Data.cloud_color,
                     [x_position + 6, y_position + 8, 18, 10])

  def start_game(self):
    while not Data.done:
      # Event processing (React to key presses, mouse clicks, etc.)
      ''' for now, we'll just check to see if the X is clicked '''
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          Data.done = True
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_l:
            Data.lights_on = not Data.lights_on
          elif event.key == pygame.K_d:
            Data.day = not Data.day

      # Game logic (Check for collisions, update points, etc.)
      ''' leave this section alone for now '''
      if Data.lights_on:
        Data.light_color = Color.YELLOW
      else:
        Data.light_color = Color.SILVER

      if Data.day:
        Data.sky_color = Color.BLUE
        Data.field_color = Color.GREEN
        Data.stripe_color = Color.DAY_GREEN
        Data.cloud_color = Color.WHITE
      else:
        Data.sky_color = Color.DARK_BLUE
        Data.field_color = Color.DARK_GREEN
        Data.stripe_color = Color.NIGHT_GREEN
        Data.cloud_color = Color.NIGHT_GRAY

      for c in Data.clouds:
        c[0] -= 0.5

        if c[0] < -100:
          c[0] = random.randrange(800, 1600)
          c[1] = random.randrange(0, 150)

      # Drawing code (Describe the picture. It isn't actually drawn yet.)
      Data.screen.fill(Data.sky_color)
      Data.SEE_THROUGH.fill(Color.ck)
      Data.SEE_THROUGH.set_colorkey(Color.ck)

      if not Data.day:
        #stars
        for s in Data.stars:
          pygame.draw.ellipse(Data.screen, Color.WHITE, s)

      #field
      Graphics_Drawer.draw_field()

      #fence
      Graphics_Drawer.draw_fence()

      for c in Data.clouds:
        self.draw_cloud(c[0], c[1])
      Data.screen.blit(Data.SEE_THROUGH, (0, 0))

      #out of bounds lines
      Graphics_Drawer.draw_boundary_lines()

      #safety circle
      Graphics_Drawer.draw_safety_circle()

      #18 yard line goal box with arc above it
      Graphics_Drawer.draw_18_yard_box()

      Graphics_Drawer.draw_score_board()

      #goal
      Graphics_Drawer.draw_goal()

      #6 yard line goal box
      Graphics_Drawer.draw_6_yard_box()

      #flood lights
      Graphics_Drawer.draw_flood_light_1()
      Graphics_Drawer.draw_flood_light_2()

      #net
      Graphics_Drawer.draw_net()

      #stands
      Graphics_Drawer.draw_stands()

      #corner flags
      Graphics_Drawer.draw_corner_flags()

      # DARKNESS
      if not Data.day and not Data.lights_on:
        Data.screen.blit(Data.DARKNESS, (0, 0))

      #pygame.draw.polygon(screen, BLACK,
      #                    [[200, 200], [50,400], [600, 500]], 10)

      ''' angles for arcs are measured in radians (a pre-cal topic) '''
      #pygame.draw.arc(screen, ORANGE, [100, 100, 100, 100], 0, math.pi/2, 1)
      #pygame.draw.arc(screen, BLACK, [100, 100, 100, 100], 0, math.pi/2, 50)


      # Update screen (Actually draw the picture in the window.)
      pygame.display.flip()


      # Limit refresh rate of game loop
      Data.clock.tick(Data.refresh_rate)


    # Close window and quit
    pygame.quit()


if __name__ == "__main__":
  test = graphics_v4()
