from datetime import datetime, timedelta, timezone

now = datetime.now()
print(now)
tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
dt = now.replace(tzinfo=tz_utc_8) # 强制设置为UTC+8:00
print(dt)

# 时区转换
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_dt)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)

dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
print(dt)
# 秒为单位
print(dt.timestamp())
# datetime转换为str
print(now.strftime('%a, %b %d %H:%M'))
print(now + timedelta(days=1, hours=10))



