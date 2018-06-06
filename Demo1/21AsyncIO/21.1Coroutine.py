# 子程序(函数)就是协程的一种特例
#
# 首先调用c.send(None)启动生成器；
#
# 然后，一旦生产了东西，通过c.send(n)切换到consumer执行；
#
# consumer通过yield拿到消息，处理，又通过yield把结果传回；
#
# produce拿到consumer处理的结果，继续生产下一条消息；
#
# produce决定不生产了，通过c.close()关闭consumer，整个过程结束。
#
# 整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。


def producer(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[Producer] Producing %s...' % n)
        r = c.send(n)
        print('[Producer] consuer returns r = %s ' % r)
    c.close()

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

c = consumer()
producer(c)