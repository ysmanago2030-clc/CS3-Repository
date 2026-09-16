class Glassware:
    pass

class Beaker (Glassware):
    pass

class Tray:
    def __init__(self):
        self.beakers = [Beaker() for i in range (5)]
        
