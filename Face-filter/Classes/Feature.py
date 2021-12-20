class Feature:
    def __init__(self, is_tilted):
        self.rects = []
        self.is_tilted = is_tilted

    def add_rect(self, rect):
        self.rects.append(rect)