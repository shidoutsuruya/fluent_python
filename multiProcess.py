import threading
import time
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

def task():
    time.sleep(2)
    name=threading.currentThread().getName()
    print(name)
#*daemon:when main end,thread automatically end

t=threading.Thread(target=task,daemon=True,name='task!!!')
t.start()

if __name__ == '__main__':
    time.sleep(3)
    print('hello')

 