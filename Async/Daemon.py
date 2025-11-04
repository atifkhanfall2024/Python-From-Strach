import threading
import time


def ChaiTime():

    while True:
        print('Chai Time or waiting till now ')
        time.sleep(3)

t = threading.Thread(target=ChaiTime)
t.start()
print('Main program is done')

