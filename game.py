from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# Environment (Ground and Walls)
ground = Entity(model='plane', scale=(100, 1, 100), color=color.lime, texture='white_cube')
wall = Entity(model='cube', position=(0, 1, 10), scale=(10, 5, 1), color=color.gray)

# Player (First Person Controller)
player = FirstPersonController()
player.cursor.visible = True

# Bullet list
bullets = []

def input(key):
    if key == 'left mouse down':
        # Shoot a small bullet sphere
        bullet = Entity(model='sphere', color=color.yellow, scale=0.8, position=player.position + Vec3(0, 0.9, 0))
        bullet.velocity = player.forward * 40
        bullets.append(bullet)

def update():
    # Move bullets forward
    for bullet in bullets:
        bullet.position += bullet.velocity * time.dt

app.run()