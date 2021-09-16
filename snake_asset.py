import random
import copy


class SnakeBlock:
    """Snake block class"""

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def update_position(self):
        if self.direction == "N":
            self.y -= 1
        elif self.direction == "S":
            self.y += 1
        elif self.direction == "E":
            self.x += 1
        else:
            self.x -= 1

    def get_pos(self):
        return (self.x, self.y)

    def has_collided(self):
        return self.x > 9 or self.x < 0 or self.y < 0 or self.y > 9

    def create_copy(self):
        return copy.deepcopy(self)


class AppleBlock:
    def __init__(self, possible_pos):
        pos = random.choice(possible_pos)
        self.x = pos[0]
        self.y = pos[1]

    def location(self):
        return self.x, self.y


