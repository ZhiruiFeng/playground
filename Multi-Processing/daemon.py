import multiprocessing
import time
import sys

def daemon():
    p = multiprocessing.current_process()
    print 'starting :',p.name, p.pid
    sys.stdout.flush()
    for i in range(3):
        print 'Sleep time:', p.name, i
        sys.stdout.flush()
        time.sleep(2)
    print 'Exiting :',p.name, p.pid
    sys.stdout.flush()

def non_daemon():
    p = multiprocessing.current_process()
    print 'Starting:', p.name, p.pid
    sys.stdout.flush()
    print 'Exiting :', p.name, p.pid
    sys.stdout.flush()

if __name__ == '__main__':
    d = multiprocessing.Process(name='daemon', target=daemon)
    d.daemon = True

    d1 = multiprocessing.Process(name='daemon1', target=daemon)
    d1.daemon = True
    
    n = multiprocessing.Process(name='non-daemon', target=non_daemon)
    n.daemon = False
    n1 = multiprocessing.Process(name='non-daemon1', target=non_daemon)

    d.start()
    time.sleep(2)
    d1.start()
    n.start()
    d.join()
    d1.join()
    n1.start()
