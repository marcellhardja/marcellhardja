import pygame
from math import sin,cos, sqrt, atan2
import pygame.surfarray
from bullet import Bullet

def gen_pendulum_physics_Heun(dt, theta0, theta_dot0, m, g, l):
    a = float(-m * g * l)
    b = float(m * l * l)
    # initialize generalized coordinates
    q = theta0
    p = theta_dot0
    while True:
        # Update using Heun's Method
        q_dot1 = p / b
        p_dot1 = a * sin(q)
        q_dot2 = (p + dt * p_dot1) / b
        p_dot2 = a * sin(q + dt * q_dot1)
        q += dt / 2.0 * (q_dot1 + q_dot2)
        p += dt / 2.0 * (p_dot1 + p_dot2)
        yield q

COLOR = {'black': (0, 0, 0),
         'red': (255, 0, 0),
         'green': (0, 255, 0),
         'blue': (0, 0, 255)}

# initialize bullet class
bullet = Bullet(screen=(800,800))
# make the speed_factor from bullet class into variable
speed = bullet.speed_factor


PHYSICS_GENERATORS = {
    'Heun': gen_pendulum_physics_Heun}

class Pendulum(pygame.sprite.Sprite):
    """renders a fixed pivot pendulum and updates motion according to differential equation"""

    def __init__(self, pivot_vect, length, bob_radius, bob_mass, init_angle,
                 integration_method='Heun'):
        pygame.sprite.Sprite.__init__(self)
        # Initialize the integration method
        phys_gen_init = PHYSICS_GENERATORS[integration_method]
        # Inputting the information needed for the pendulum
        self.phys_gen = phys_gen_init(dt=0.01*speed, theta0=init_angle, theta_dot0=0, m=bob_mass, g=9.8, l=length / 1000.0)
        self.length = length
        self.bob_radius = bob_radius
        self.bob_mass = bob_mass
        self.angle = init_angle
        self.pivot_vect = pivot_vect
        # Vector from top left to pivot of pendulum
        swinglen = (length + bob_radius)  # whole
        # To convert the pixel of the image to be the same so converting wont need to be done over and over
        # Create surface just big enough to fit swing
        self.image = pygame.Surface((swinglen * 2, swinglen * 2)).convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = (pivot_vect[0] - swinglen, pivot_vect[1] - swinglen)  # place so that pivot is at center
        # Calculate the initial relative bob position in the image
        self.bob_X = int(length * sin(init_angle) + self.rect.width // 2)
        self.bob_Y = int(length * cos(init_angle) + self.rect.height // 2)
        self.bob_rect = None
        # render the pendulum from the parameters
        self.render()

    def render(self):
        # Pendulum surface
        self.image.fill(COLOR['black'])
        bob_pos = (self.bob_X, self.bob_Y)
        # Draw the line
        pygame.draw.aaline(self.image, COLOR['red'], (self.rect.width // 2, self.rect.height // 2), bob_pos, True)
        # draw the bob
        self.bob_rect = pygame.draw.circle(self.image, COLOR['blue'], bob_pos, self.bob_radius, 0)

    def update(self):
        # Updating the coordinates
        self.angle = self.phys_gen.__next__()
        angle = self.angle
        length = self.length
        X = int(length * sin(angle))
        Y = int(length * cos(angle))
        self.bob_X = X + self.rect.width // 2
        self.bob_Y = Y + self.rect.height // 2
        self.render()


