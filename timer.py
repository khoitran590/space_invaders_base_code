class Timer: 
  def __init__(self, image_list, start_index=0, delta=6, looponce=False): 
    self.image_list = image_list
    self.delta = delta
    self.looponce = looponce
    self.index = start_index
    self.time = 0

  def update_index(self):
    self.time += 1
    if self.time >= self.delta:
      self.index += 1
      self.time = 0
      if self.index >= len(self.image_list) and not self.looponce:
        self.index = 0

  def finished(self): 
    return self.looponce and self.index >= len(self.image_list)
  
  def current_index(self): return self.index

  def current_image(self):     # self.time = 0
    self.update_index()
    return self.image_list[self.index]
  
  # class TimerDict(Timer):
    def __init__(self): pass
    super().__init__(...)
    self.dictionary = dictionary
    self.current_key = self.start_key
    self.start_key = start_key
    
    def has_name(self, name): pass
    def keys(self): pass 
    def switch_to(self, key): pass
    
    def update_index(self): pass
    def finished(self): pass
    def current_index(self): pass
    def current_image(self): pass  #