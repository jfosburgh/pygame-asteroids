import pygame


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius) -> None:
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen) -> None:
        pygame.draw.circle(
                screen,
                pygame.Color("white"),
                self.position,
                self.radius,
                2
        )

    def update(self, dt) -> None:
        self.position += dt * self.velocity

    def collides(self, other) -> bool:
        return self.position.distance_to(other.position) < self.radius + other.radius
