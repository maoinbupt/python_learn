from multiprocessing import Process
import os


# multiprocessing模块就是跨平台版本的多进程模块
def run_proc(name):
    print('Run process %s(%s)' % (name, os.getpid()))

if __name__ == '__main__':
    print('Parent process %s' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start')
    p.start()
    p.join()
    print('CHild process ENd')