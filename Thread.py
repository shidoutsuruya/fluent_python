import threading
import time
import os
#*threading test
num=0
def _add(count):
    global num
    for _ in range(count):
        num+=1
        print(num)
def _sub(count):
    global num
    for _ in range(count):
        num-=1
        print(num)
"""      
t1=threading.Thread(target=_add,args=(100,))
t2=threading.Thread(target=_sub,args=(100,))
t1.start()
t2.start()
t1.join()
t2.join()
"""  
#*Daemon
"""
def task():
    time.sleep(2)
    name=threading.currentThread().getName()
    print(name)
#*daemon:when main end,thread automatically end

t=threading.Thread(target=task,daemon=True,name='task!!!')
t.start()
"""

def task1():
    print(f'task1 thread:{threading.current_thread().name}')
    print(f'task1 process ID:{os.getpid()}')
def task2():
    print(f'task2 thread:{threading.current_thread().name}')
    print(f'task2 process ID:{os.getpid()}')
if __name__ == '__main__':
    print(f'Main thread name:{threading.current_thread().name}')
    t1=threading.Thread(target=task1,name='t1')
    t2=threading.Thread(target=task2,name='t2')
    t1.start()
    t2.start()
    t1.join()
    t2.join()