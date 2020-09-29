import threading
import time

class MyThread(threading.Thread):
    def __init__(self, thread_name):
        super(MyThread, self).__init__(name=thread_name)

    def run(self):
        print("%s is running..." %self.name)

if __name__ == '__main__':
    for i in range(10):
        MyThread("thread " + str(i)).start()

def func():
    print(threading.current_thread().getName(), "start running")
    time.sleep(2)
    print("sub thread end")

for i in range(3):
    t = threading.Thread(target=func)
    t.start()
time.sleep(1)
print("main thread end")