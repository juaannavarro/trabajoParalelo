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




