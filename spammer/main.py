import time
import api

i = 0
while True:
    i += 1
    api.log(i)
    time.sleep(5)
