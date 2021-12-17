import multiprocessing
import time
def sing(num):
    for i in range(num):
        print("sing sing sing")
        time.sleep(0.5)
def dance(num):
    for i in range(num):
        print('dance '*3)
        time.sleep(0.5)
        
if __name__ == '__main__':
    sing_process=multiprocessing.Process(target=sing,args=(3,))
    dance_process=multiprocessing.Process(target=dance,kwargs={"num":3})
    sing_process.start()
    dance_process.start()