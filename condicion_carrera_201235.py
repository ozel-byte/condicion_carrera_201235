import pygame
from os import scandir
from os.path import abspath
import threading
import time
import random


lista_music = []
p = pygame
class Rocola:
    def __init__(self) -> None:
        self.lock = threading.Lock()
        
    def reproducir(self,name_music):
        self.lock.acquire()
        try:
            p.init()
            p.mixer.music.load("music/"+name_music)
            print(f"Cancion en reproduccion: {name_music}")
            p.mixer.music.play()
            clock = p.time.Clock()
            contador = 0
            while p.mixer.music.get_busy():
                clock.tick(60)
                if contador == 1000:
                    p.mixer.music.stop()
                else:
                    p.event.poll()
               
                contador+=1
        finally:
            self.lock.release()


def ls(ruta = "music/"):
    return [arch.name for arch in scandir(ruta) if arch.is_file()]


def iniciar_music(x,name_music):
    x.reproducir(name_music)
    time.sleep(2)


if __name__ == "__main__":
    lista_music = ls()
    rocola = Rocola()
    for x in range(2):
       t_start = threading.Thread(target=iniciar_music, args=(rocola,lista_music[random.randrange(len(lista_music))]))
       t_start.start()