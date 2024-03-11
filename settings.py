class Settings:
  def __init__(self):
    self.screen_width = 1200
    self.screen_height = 700
    self.bg_color = (70, 70, 70)

    self.laser_width = 5
    self.laser_height = 15
    self.laser_color = (255, 0, 0)

    self.alien_spacing = 1.2
    self.fleet_drop = 10

    self.ship_limit = 3

    self.speedup_scale = 1.5
    self.score_scale = 1.5

    self.aliens_fireevery = 30
    
    self.initialize_dynamic_settings()

  def initialize_dynamic_settings(self):
    self.laser_speed = 10
    self.alien_speed = 10
    self.ship_speed = 15

    self.alien_points = 50

  def increase_speed(self):
    # self.laser_speed *= self.speedup_scale
    self.alien_speed *= self.speedup_scale
    # self.ship_speed *= self.speedup_scale

    self.alien_points = int(self.alien_points * self.score_scale)


if __name__ == '__main__':
  print("\nERROR: settings.py is the wrong file! Run play from alien_invasions.py\n")
