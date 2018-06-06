from multiprocessing import Pool
import os, time, random


# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
def long_time_task(name):
    print('Run task %s (%s) ' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print(' task %s runs %0.2f seconds ' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting all subprocess done')
    p.close()
    p.join()
    print('All subprocess done')

import subprocess

# subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# 子进程还需要输入，则可以通过communicate()方法输入
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)
