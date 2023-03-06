# trabajoParalelo

#   CÓDIGO PARALELO:
```
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

```
#   CÓDIGO SECUENCIAL:
```
import random
from time import sleep
import time



def scrape(url):
        print("starting", url)
        duration = round(random.random(), 3)
        sleep(duration)
        print("finished", url, "time taken:", duration, "seconds") #imprime la url que se ha raspado, el tiempo que ha tardado en rasparla y el tiempo que ha tardado en rasparla.
        return url, duration

urls = ["a.com", "b.com", "c.com", "d.com"]
```
#   CÓDIGO MAIN:
```
from paralelo import *
#from secuencial import *


if __name__ == "__main__":
    while True:
        print("1. Paralelo")
        print("2. Secuencial")
        print("3. Comparar")
        print("4. Salir")
        opcion = input("Ingrese una opcion: ")
        if opcion == "1":
            start= time.time()
            pool = Pool(processes=4)  #creamos el pool de procesos con el número de procesos que queremos que se ejecuten en paralelo.
            data = pool.map(scrape, urls) #creamos data para recoger las urls y el tiempo que tarda en rasparlas.Luego map llama a la funcion scrape con cada url y guarda el resultado en data.
            pool.close()    #cerramos el pool de procesos.
            print()
            for row in data:   #imprimimos data,(las urls y el tiempo que tarda en rasparlas).
                print((row))
            end = time.time()         
            print("Total time taken:", end - start, "seconds")
            def guardar_paralelo():
                tiempo = end - start
                print("El tiempo total de ejecucion en paralelo es: ", tiempo)
            

        elif opcion == "2":
            start1= time.time()
            output = []
            for url in urls:
                result = scrape(url)
            output.append(result)
            end1 = time.time()
            print("Total time taken:", end1 - start1, "seconds")
            def guardar_secuencial():
                tiempo1 = end1 - start1
                print("El tiempo total de ejecucion en secuencial es: ", tiempo1)
            
        elif opcion == "3":
            print("Comparar")
            guardar_paralelo()
            guardar_secuencial()
        else:
            print("Opcion invalida")
            break


```


