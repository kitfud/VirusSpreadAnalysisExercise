import pygame
from pygame.locals import * 
import random

from virus import VirusNode 
from doctor import Doctor

pygame.init()

size = (width, height) = (850, 480) 
screen = pygame.display.set_mode(size) 
clock = pygame.time.Clock()

color = (26, 255, 255)

bacteria = pygame.sprite.Group() 
doctors = pygame.sprite.Group()

doc_num = 1 
bac_num = 5 
split_time = 500 
done = False

def process_events(): 
  global done
  for event in pygame.event.get(): 
    if event.type == pygame.QUIT:
      done = True


def main():
  bacteria.add(VirusNode((random.randint(50,width-50),random.randint(50,height-50)),split_time))
  doctors.add(Doctor((random.randint(50,width-50),random.randint(50,height-50))))

  while not done:
    clock.tick(60) 
    process_events()

    doctors.update()
    bacteria.update() 

    screen.fill(color) 
    doctors.draw(screen) 
    bacteria.draw(screen) 
    pygame.display.flip()

if __name__ == "__main__":
  main()

