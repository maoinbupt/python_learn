name = input("please enter your name")
print("hello " + name)

#字符串格式化
print('Hi, %s, you have $%d.' % ('Michael', 1000000))

sum = 0
for i in range(1,5,2):
    sum +=i

print(sum)


dictD = {'mike':'abc','gf':2, 'xk':3}
print(dictD['mike'])



s1 = set([1,2,3])
s2 = set([2,3,4])

#list
l1 = [1,2]

#tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
t1 = (1,2,3)
t2 = (1,2,[1,2])
s1.add(t1)
# tuple虽然是不变对象,t1不可变，t2可变
# s1.add(t2)

# 不能添加可变对象
# s1.add(l1)
print(s1&s2)
#交集{2,3}
print(s1|s2)
#并集{1,2,3,4}
