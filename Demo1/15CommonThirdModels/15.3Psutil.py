import psutil


# psutil = process and system utilities，它不仅可以通过一两行代码实现系统监控，还可以跨平台使用
# CPU逻辑数量
print(psutil.cpu_count())

# CPU物理核心
print(psutil.cpu_count(logical=False))

# 统计CPU的用户／系统／空闲时间：
print(psutil.cpu_times())

# 实现类似top命令的CPU使用率，每秒刷新一次，累计10次
for x in range(5):
     print(psutil.cpu_percent(interval=1, percpu=True))

# 获取物理内存和交换内存信息
print(psutil.virtual_memory())
print(psutil.swap_memory())

# 磁盘分区、磁盘使用率和磁盘IO信息
print(psutil.disk_partitions())
print(psutil.disk_usage('/'))
print(psutil.disk_io_counters())

# 获取网络读写字节／包的个数
print(psutil.net_io_counters())
# 获取网络接口信息
print(psutil.net_if_addrs())
# 获取网络接口状态
print(psutil.net_if_stats())
# 获取当前网络连接信息
# 可能会得到一个AccessDenied错误
# print(psutil.net_connections())

print(psutil.pids())

# 获取指定进程ID=3776，其实就是当前Python交互环境
p = psutil.Process()
print(p.name())
print(p.terminate)