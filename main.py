from paralelo import *
#from secuencial import *


if __name__ == "__main__":
    while True:
        print("1. Paralelo")
        print("2. Secuencial")
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
            

        elif opcion == "2":
            start= time.time()
            output = []
            for url in urls:
                result = scrape(url)
            output.append(result)
            
            end = time.time()
            print("Total time taken:", end - start, "seconds")
            
            
        else:
            print("Opcion invalida")
            break




