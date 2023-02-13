# trabajoParalelo


from multiprocessing import Pool #importamos el multiprocesamiento para que se ejecute en paralelo y no uno por uno.
from time import sleep
import random
def scrape(url): #funcion que raspa las urls.
    print("starting", url) #imprimimos las urls que se esta raspando.
    duration = round(random.random(),3) #creamos una variable duration que es un numero aleatorio entre 0 y 1 con 3 decimales.
    sleep(duration) #hacemos que el programa espere el tiempo que dura la variable duration.
    print("finished", url, "time taken:", duration, "seconds") #imprime la url que se ha raspado, el tiempo que ha tardado en rasparla y el tiempo que ha tardado en rasparla.
    return url, duration
url = ["a.com", "b.com", "c.com", "d.com"]  #lista de urls que queremos raspar.
if __name__ == "__main__":
    pool = Pool(processes=4)  #creamos el pool de procesos con el número de procesos que queremos que se ejecuten en paralelo.
    data = pool.map(scrape, url) #creamos data para recoger las urls y el tiempo que tarda en rasparlas.Luego map llama a la funcion scrape con cada url y guarda el resultado en data.
    pool.close()    #cerramos el pool de procesos.
    print()
    for row in data:   #imprimimos data,(las urls y el tiempo que tarda en rasparlas).
        print(row)
