import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen) -> None:
        super().draw(screen)

    def update(self, dt) -> None:
        super().update(dt)

    def split(self) -> None:
        self.kill()

        if self.radius < ASTEROID_MIN_RADIUS:
            return

        rotation_offset = random.uniform(20, 50)
        radius = self.radius - ASTEROID_MIN_RADIUS

        x, y = self.position.x, self.position.y
        Asteroid(x, y, radius).velocity = self.velocity.rotate(rotation_offset) * 1.2
        Asteroid(x, y, radius).velocity = self.velocity.rotate(-rotation_offset) * 1.2

