#!/usr/bin/python3

import os
from multiprocessing.pool import ThreadPool
import time

 #timesToRun = 1000
timesToRun = 1000

# should be one less than the number of logical processors your computer has
# mine has 32 so 31 is used
numCores = 31

command = "./gnu/gnu 3"
#command = "sleep 1"
#command = "ls > /dev/null"

totalTime = time.time() - time.time()

def handleThread():
    print("starting test...")
    starttime = time.time()
    os.system(command,)
    time_ = time.time() - starttime

    print("ending test")
    return time_

results = []

def main():
    pool = ThreadPool(processes=numCores)

    global totalTime

    for _ in range(0, timesToRun):
        results.append(pool.apply_async(handleThread, ()))
    
    for result in results:
        totalTime += result.get()

    print("processing...")
    
    print(totalTime)


if __name__ == '__main__':
    main()

