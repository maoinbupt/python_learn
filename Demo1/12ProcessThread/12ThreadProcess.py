import os

print('Process %s start~~' % os.getpid())

# Only works on Unix/Linux/Mac:
# 当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。
# 子进程永远返回0，而父进程返回子进程的ID
# 常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，就fork出子进程来处理新的http请求。
pid = os.fork()

if pid == 0:
    print('I am child process %s and my parent is %s ' % (os.getpid(), os.getppid()))
else:
    print('I %s just create a child process %s ' % (os.getpid(), pid))


from multiprocessing import Process

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

print('Parent process %s.' % os.getpid())
p = Process(target=run_proc, args=('test',))
print('Child process will start.')
p.start()
p.join()
print('Child process end.')


from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

print('Parent process %s.' % os.getpid())
p = Pool(4)
for i in range(5):
    p.apply_async(long_time_task, args=(i,))
print('Waiting for all subprocesses done...')
p.close()
p.join()
print('All subprocesses done.')



import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)