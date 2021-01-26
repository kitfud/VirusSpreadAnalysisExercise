import pygame
from pygame.locals import * 
import random

from virus import VirusNode 
from doctor import Doctor
pygame.init()

font = pygame.font.SysFont(None, 70)
split_times = 10



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

def init():
  for i in range(bac_num):
    bacteria.add(VirusNode((random.randint(50, width-50),random.randint(50, height-50)), split_time))
  for i in range(doc_num):
    doctors.add(Doctor((random.randint(50, width-50),random.randint(50, height-50))))

def main():
  bacteria.add(VirusNode((random.randint(50,width-50),random.randint(50,height-50)),split_time))
  doctors.add(Doctor((random.randint(50,width-50),random.randint(50,height-50))))

  init()
  while not done:
    clock.tick(60) 
    process_events()
    if len(bacteria) > 9:
      text = font.render("You were overrun", True, (255, 0,0))
      text_rect =text.get_rect()
    elif len(bacteria) == 0:
      text = font.render("Outbreak stopped", True, (255, 0,0))
      text_rect = text.get_rect()
    else:
      doctors.update()
      bacteria.update()
      pygame.sprite.groupcollide(doctors, bacteria, False,True)
      text = font.render("Bacteria Count: {}".format(len(bacteria)), True, (255, 0, 0))
      text_rect = text.get_rect()

    screen.fill(color) 
    doctors.draw(screen) 
    bacteria.draw(screen)
    screen.blit(text,text_rect) 
    pygame.display.flip()

if __name__ == "__main__":
  main()

