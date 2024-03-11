import pygame as pg
from pygame.sprite import Sprite


class BarrierPiece(Sprite):
    def __init__(self, game, x, y):
        super().__init__()
        self.screen = game.screen
        self.image = pg.Surface((10, 10))  # Size of the barrier piece
        self.image.fill((0, 255, 0))  # Fill the piece with green color
        self.rect = self.image.get_rect(topleft=(x, y))
    
    def draw(self):
        self.screen.blit(self.image, self.rect)


class Barrier:
    def __init__(self, game, x, y, rows=4, cols=10):
        self.barrier_piece_group = pg.sprite.Group()
        self.game = game
        piece_width = 10  # Assuming each piece is 10 pixels wide
        piece_height = 10  # Assuming each piece is 10 pixels tall
        for row in range(rows):
            for col in range(cols):
                piece_x = x + col * piece_width
                piece_y = y + row * piece_height
                piece = BarrierPiece(game, piece_x, piece_y)
                self.barrier_piece_group.add(piece)

    def update(self):
        # This method can be used to check for collisions and remove destroyed pieces
        pass

    def draw(self):
        for piece in self.barrier_piece_group:
            piece.draw()

class Barriers:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.barriers = []
        self.create_barriers()

    def create_barriers(self):
        barrier_x_start = 100  # Starting X position for the first barrier
        barrier_y = 450  # Y position for all barriers
        barrier_spacing = 100  # Space between each barrier
        for i in range(4):
            b = Barrier(self.game, barrier_x_start + i * (barrier_spacing + 40), barrier_y)
            self.barriers.append(b)

    def update(self):
        for b in self.barriers:
            b.update()

    def draw(self):
        for b in self.barriers:
            b.draw()