from multiprocessing import Process
import datetime
import time

def t(s):
    while True:
        time.sleep(1.1)
        print(datetime.datetime.now().time())

def main():
    rep = 0
    p = Process(target=t, args=(1,))
    p.start()

    while rep < 10:
        time.sleep(0.5)
        print(p.pid)
        rep=rep+1

    p.terminate()
    print("fi")

if __name__ == '__main__':
    main()
