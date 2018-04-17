import multiprocessing
import time
import sys

def slow_worker():
    print 'Starting worker'
    sys.stdout.flush()
    time.sleep(0.1)
    print 'Finished worker'
    sys.stdout.flush()

if __name__ == '__main__':
    p = multiprocessing.Process(target=slow_worker)
    p.daemon =True
    print 'BEFORE:', p, p.is_alive()
    
    p.start()
    print 'DURING:', p, p.is_alive()
    #time.sleep(0.01)
    #p.terminate()
    #print 'TERMINATED:', p, p.is_alive()

    
    print 'JOINED:', p, p.is_alive()
    p.join()
