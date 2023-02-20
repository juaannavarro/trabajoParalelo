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

 



