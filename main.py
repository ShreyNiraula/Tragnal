import threading
from tragnal2 import app

from koteshworSeqGenerator import *
from jadibutiSeqGenerator import *
from lokanthaliSeqGenerator import *

def weFlask():
	app.run()

t1 = threading.Thread(target=weFlask,)
t2 = threading.Thread(target = koteshworSeqGenerationFunction,)
t3 = threading.Thread(target = jadibutiSeqGenerationFunction,)
t4 = threading.Thread(target = lokanthaliSeqGenerationFunction,)

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()





