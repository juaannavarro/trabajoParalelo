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

<img width="435" alt="Captura de pantalla 2023-03-06 a las 17 17 20" src="https://user-images.githubusercontent.com/91721668/223168782-d65e052d-043f-4c5e-be37-2e3622b3b387.png">


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
<img width="456" alt="Captura de pantalla 2023-03-06 a las 17 17 32" src="https://user-images.githubusercontent.com/91721668/223168863-fb1e41e4-fd1a-4c3e-87da-90a254c05a42.png">


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

1.Captura en el momento de ejecutar el menú:
<img width="144" alt="Captura de pantalla 2023-03-06 a las 17 18 23" src="https://user-images.githubusercontent.com/91721668/223168912-9a4c3344-190e-4045-bee9-24280d917c2e.png">


2.Captura ejecutando el paralelo:
<img width="435" alt="Captura de pantalla 2023-03-06 a las 17 17 20" src="https://user-images.githubusercontent.com/91721668/223168956-39cdcc1c-b9ee-41f9-8d75-c29e5b46795f.png">


3.Captura ejecutando el secuencial:
<img width="456" alt="Captura de pantalla 2023-03-06 a las 17 17 32" src="https://user-images.githubusercontent.com/91721668/223168983-a0c2dfc1-718a-4da5-a528-b84654e665c5.png">


4.Captura comparando tiempos
<img width="570" alt="Captura de pantalla 2023-03-06 a las 17 17 43" src="https://user-images.githubusercontent.com/91721668/223169000-3a10d814-4599-44c2-b465-1b7790d3df72.png">

# Conclusión

Como podemos observar, el tiempo en paralelo es mucho menor al secuencial en la mayoría de los casos.
