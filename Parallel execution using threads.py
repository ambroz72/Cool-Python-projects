import time
from threading import Thread

def task1():
    print("Starting Ops 1")
    time.sleep(2)
    print("Ops 1 completed")

def task2():
    print("Starting Ops 2")
    time.sleep(3)
    print("Ops 2 completed")

t1 = Thread(target=task1)
t1.start()
t2 = Thread(target=task2)
t2.start()


    
