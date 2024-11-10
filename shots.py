from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y) -> None:
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen) -> None:
        super().draw(screen)

    def update(self, dt) -> None:
        super().update(dt)
