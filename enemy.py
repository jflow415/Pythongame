from gameObject import GameObject

class Enemy(GameObject):

    def __init__(self, x, y, width, height, image_path, speed):
        super().__init__(x, y, width, height, image_path)

        self.speed = speed


    #create enemy to move left to right
    def move(self, max_width):
        #create borders
        if self.x <= 0:
            self.speed = abs(self.speed)
        elif self.x >= max_width - self.width:
            self.speed = -self.speed
            
        self.x += self.speed


