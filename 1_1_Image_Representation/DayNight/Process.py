from DayNight.Load import Load
from DayNight.Transform import Transform

class Process(object):
    def __init__(self, load, transforms):
        self.load = load
        self.transforms = transforms

    def transforms_load(self):
        pass
        
