import numpy as np
jzsize = 3
juzhen = np.array([[1,3,5],
                  [0.33,1,2],
                  [0.2,0.5,1]])

def fuzhi(i,jzlen):                          #重复操作多次用函数封装起来
    xxx = juzhen*np.mat(y100[:,i-1]).T       #先求出矩阵和y的第i-1列相乘，把新矩阵赋给xxx
    for h in range(jzlen):                   #此for循环用来把xxx矩阵的内容赋给x的第i列，之所以用for循环赋值是因为x[:,i]是一个一维数组
        x100[h][i] = xxx.tolist()[h][0]      #而xxx是一个二维矩阵，所以就用中间变量xxx承接了一下，中间进行了一些操作，目的是把y的i-1列赋给x的第i列
    print(x100[:,i])
    middle[i] = x100[:,i].max()
    y100[:,i] = x100[:,i]/middle[i]

x100 = np.ones((jzsize,100))
y100 = np.ones((jzsize,100))
middle = np.zeros(100)
middle[0] = x100[:,0].max()
y100[:,0] = x100[:,0]
### xxx = jz*np.mat(y100[:,0]).T
#### x100[:,1]
fuzhi(1,jzsize)
print(middle)
op = 0.0001; i=1; kl = abs(middle[1]-middle[0])
while kl>op:
    i = i+1;
    fuzhi(i,jzsize)
    kl = abs(middle[i]-middle[i-1])
dsa = sum(y100[:,i])
qwe = y100[:,i]/dsa
tyu = middle[i]

print(qwe)
print("最大特征值",tyu)

####一致性检验
CI = (tyu-jzsize)/(jzsize-1)
RI = [0, 0, 0.52, 0.89, 1.12, 1.26, 1.36, 1.41, 1.46, 1.49, 1.52, 1.54, 1.56, 1.58, 1.59]
CR = CI/RI[jzsize-1]
if CR<0.1:
    print("此矩阵的一致性可以接受")
    print('CI=',CI)
    print('CR=',CR)
else:
    print('此矩阵还需优化')
    print('CI=',CI)
    print('CR=',CR)
