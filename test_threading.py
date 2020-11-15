import threading
import time

def toothbrush(name):
	for i in range(10):
		print("{} toothbrushing {}".format(name,i))
		time.sleep(1)

def shower(name):
	for i in range(15):
		print("{} showering {}".format(name,i))
		time.sleep(1)

task1 = threading.Thread(target=toothbrush,args=('Mr.A',))
task2 = threading.Thread(target=shower,args=('Mr.B',))

time1 = time.time()

task1.start()
task2.start()

task1.join()
task2.join()

time2 = time.time()

Final = time2-time1
print(Final)