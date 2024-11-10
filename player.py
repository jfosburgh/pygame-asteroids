import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SHOOT_SPEED, PLAYER_SHOT_COOLDOWN, PLAYER_SPEED, PLAYER_TURN_SPEED
from shots import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = PLAYER_SHOT_COOLDOWN

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen) -> None:
        pygame.draw.polygon(
                screen,
                pygame.Color(255, 255, 255),
                self.triangle(),
                2
        )

    def rotate(self, dt) -> None:
        self.rotation += dt * PLAYER_TURN_SPEED

    def move(self, dt) -> None:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * dt * PLAYER_SPEED

    def update(self, dt) -> None:
        keys = pygame.key.get_pressed()
        self.shot_cooldown -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE] and self.shot_cooldown < 0:
            self.shoot()
            self.shot_cooldown = PLAYER_SHOT_COOLDOWN

    def shoot(self) -> None:
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
