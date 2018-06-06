print("hello world")
sum = 0
for i in range(1,5,2):
    sum +=i

print(sum)


dictD = {'mike':'abc','gf':2, 'xk':3}
print(dictD['mike'])



s1 = set([1,2,3])
s2 = set([2,3,4])

l1 = [1,2]

t1 = (1,2,3)
t2 = (1,2,[1,2])
s1.add(t1)
# tuple虽然是不变对象,t1不可变，t2可变
# s1.add(t2)

# 不能添加可变对象
# s1.add(l1)
print(s1&s2)
print(s1|s2)
