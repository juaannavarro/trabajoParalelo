from multiprocessing import Pool #importamos el multiprocesamiento para que se ejecute en paralelo y no uno por uno.
from time import sleep
import random
import time


def scrape(url): #funcion que raspa las urls.
        print("starting", url) #imprimimos las urls que se esta raspando.
        duration = round(random.random(),3) #creamos una variable duration que es un numero aleatorio entre 0 y 1 con 3 decimales.
        sleep(duration) #hacemos que el programa espere el tiempo que dura la variable duration.
        print("finished", url, "time taken:", duration, "seconds") #imprime la url que se ha raspado, el tiempo que ha tardado en rasparla y el tiempo que ha tardado en rasparla.
        return url, duration
urls = ["a.com", "b.com", "c.com", "d.com"]  #lista de urls que queremos raspar.






