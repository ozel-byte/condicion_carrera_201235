import pygame
from os import scandir
from os.path import abspath
import threading
import time
import random


lista_music_v1 = [{"cancion": "urge.pm3"},{"cancion":"the creep.mp3"},{"cancion":"tiempo.mp3"}]
lista_music_v2 = []
p = pygame
class Rocola:
    def __init__(self,total_music=0) -> None:
        self.lock = threading.Lock()
        self.tm = total_music
        
    def reproducir(self,name_music):
        self.lock.acquire()
        try:
            #p.init()
            p#.mixer.music.load("music/"+name_music)
            self.tm+=1
            print(f"Cancion en reproduccion: {name_music}")
            #p.mixer.music.play()
            #clock = p.time.Clock()
            #contador = 0
            #while p.mixer.music.get_busy():
                #clock.tick(60)
                #if contador == 1000:
                    #p.mixer.music.stop()
                #else:
                    #p.event.poll()
               
                #contador+=1
        finally:
            print(f"Total de canciones reproducidas: {self.tm}")
            self.lock.release()


def ls(ruta = "music/"):
    return [arch.name for arch in scandir(ruta) if arch.is_file()]


def iniciar_music(x,name_music):
    x.reproducir(name_music)
    time.sleep(2)


if __name__ == "__main__":
    #la linea comentada de abajo es para agarrar los nombres de las canciones de la carpeta music
    #lista_music_v2 = ls()
    rocola = Rocola()
    for x in range(4):
        #si desea usar la version 2 del programa comente la la segunda liena de t_start y descomente la que esta comentada
       #t_start = threading.Thread(target=iniciar_music, args=(rocola,lista_music_v2[random.randrange(len(lista_music_v2))]))
       t_start = threading.Thread(target=iniciar_music, args=(rocola,lista_music_v1[random.randrange(len(lista_music_v1))]))
       t_start.start()
   