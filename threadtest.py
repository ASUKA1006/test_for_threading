import threading
import time


#in the function of 'def __init__(self)',
#'threadingTest.__init__(self)' is fine but 
#'super()' may be slightly better to initialize with using parent

class threadingTest(threading.Thread):
    def __init__(self):
        super(threadingTest, self).__init__()

    def run(self):
        for i in range(0, 1000):
            None


#thread1.join() -> waite to run main thread til the called thread
# on which join is invoked exits. 

if __name__ == '__main__':
    startTime = time.time()
    thread1 = threadingTest()
    thread1.start()
    thread1.join()
    print(time.time()-startTime)
        

