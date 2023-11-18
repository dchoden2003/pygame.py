import unittest
import pygame
from pygame.locals import *

class TestGame(unittest.TestCase):

    def test_screen_size(self):
        pygame.init()
        size = width, height = (800, 600)
        screen = pygame.display.set_mode(size)
        self.assertEqual(screen.get_size(), size)

    def test_screen_color(self):
        pygame.init()
        screen = pygame.display.set_mode((800,600))
        screen_fill_color = (0,225,0)
        screen.fill(screen_fill_color)
        self.assertEqual(screen.get_at((0, 0)), screen_fill_color)

    def test_road_drawing(self):
        pygame.init()
        screen = pygame.display.set_mode((800,600))
        
        road_w = 400
        pygame.draw.rect(screen, (0,0,0), (200, 0, road_w, 600))
        road_surface = screen.subsurface((200, 0, road_w, 600))
        self.assertEqual(road_surface.get_at((0, 0)), (0, 0, 0))

    def test_car_loading(self):
        pygame.init()
        car = pygame.image.load ("yellowcar1.png")
        self.assertIsNotNone(car)


class TestGameLoop(unittest.TestCase):

    def test_car2_movement(self):
        car2_loc = pygame.Rect(100, 0, 50, 100)
        height = 600
        
        car2_loc[1] += 1 
        self.assertEqual(car2_loc[1], 1)
        
        car2_loc[1] += height
        self.assertEqual(car2_loc[1], 601)
        
        car2_loc.center = 300, 0
        self.assertEqual(car2_loc.center, (300, 50))

    def test_collision(self):
        car_loc = pygame.Rect(300, 300, 50, 100)
        car2_loc = pygame.Rect(100, 100, 50, 100)
        self.assertFalse(car_loc.colliderect(car2_loc))
        
        car2_loc.center = 350, 350
        self.assertTrue(car_loc.colliderect(car2_loc))

    def test_car_movement(self):
        car_loc = pygame.Rect(300, 300, 50, 100)
        car_speed = 10
        
        pygame.key.get_pressed = lambda: [0,0,1,0] # right key
        car_loc.x += car_speed 
        self.assertEqual(car_loc.x, 310)
        
        pygame.key.get_pressed = lambda: [0,0,0,1] # left key  
        car_loc.x -= car_speed
        self.assertEqual(car_loc.x, 300)
        
if __name__ == '__main__':
    unittest.main()
        
