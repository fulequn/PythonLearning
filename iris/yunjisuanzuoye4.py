# 参考 https://www.cnblogs.com/shenxiaolin/p/8857158.html , https://blog.csdn.net/liulina603/article/details/78676723
from sklearn.linear_model import LogisticRegression  #导入逻辑回归模型
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
#多次分类问题
# 1.花萼的长、宽
# 2.花瓣的长、宽
# 3.花萼长、花瓣宽
# 4.花瓣长、花萼宽

'''
datas
labels
'''
def logistic(datas, labels, titleOfChart, x_label, y_label):
    plt.figure()#创建新画布
    datas=np.array(datas)
    datas=datas.astype(float) #将二维的字符串数组转换成浮点数数组
    labels=np.array(labels)   #150个类别，50个'Iris-setosa'，50个'Iris-versicolor'，50个'Iris-virginica'
    clf = LogisticRegression()  #获取Logistic线性回归模型
    #将字符串类型的标签转化为数字类型，进行数字编码处理
    for i in range(len(labels)):
        if labels[i] == 'Iris-setosa':
            labels[i] = 0
        elif labels[i] == 'Iris-versicolor':
            labels[i] = 1
        else:
            labels[i] = 2
    labels = labels.astype(np.int)#降低内存空间
    
    #模型建立
    clf.fit(datas, labels)#使用已有的数据和标签进行模型拟合
    
    #数据准备阶段
    N, M = 500, 500  # 横纵各采样多少个值
    x1_min, x2_min = datas.min(axis=0)
    x1_max, x2_max = datas.max(axis=0)
    t1 = np.linspace(x1_min, x1_max, N)
    t2 = np.linspace(x2_min, x2_max, M)
    x1, x2 = np.meshgrid(t1, t2)  # 生成网格采样点
    x_show = np.stack((x1.flat, x2.flat), axis=1)  # 测试点
    y_predict = clf.predict(x_show)#预测值
    
    cm_light = mpl.colors.ListedColormap(['#A0FFA0', '#FFA0A0', '#A0A0FF'])
    cm_dark = mpl.colors.ListedColormap(['g', 'r', 'b'])
    plt.pcolormesh(x1, x2, y_predict.reshape(x1.shape), shading='auto', cmap=cm_light)
    plt.scatter(datas[:,0], datas[:,1], c=labels.transpose(), cmap=cm_dark, marker='o', edgecolors='k')
   
    plt.xlim(x1_min, x1_max)
    plt.ylim(x2_min, x2_max)
    #设置x轴和y轴的标签以及主题
    plt.title(titleOfChart, fontsize=15)
    plt.xlabel(x_label, fontsize=11)
    plt.ylabel(y_label, fontsize=11)
    
    plt.show()
    
    
# 设置中文字体
mpl.rcParams["font.sans-serif"]=["SimHei"]
mpl.rcParams["axes.unicode_minus"]=False

cm_light = mpl.colors.ListedColormap(['g', 'r', 'b'])
attributes=['SepalLength','SepalWidth','PetalLength','PetalWidth'] #鸢尾花的四个属性名
#按照不同的分类标准收集数据
datas1=[]
datas2=[]
datas3=[]
datas4=[]
labels1=[]#标签列
data_file=open('iris.txt','r')
#数据初始化
for line in data_file.readlines():
    linedata = line.split(',')
    #剔除异常数据
    if len(linedata) == 5:
        linedata = np.array(linedata)  #转化为多维数组
        datas1.append(linedata[:2]) # [0:2]花萼长宽
        labels1.append(linedata[-1].replace('\n', ''))  # 获取150朵花儿所属的类别
        datas2.append(linedata[2:4]) # [2:4]花瓣长宽
        datas3.append(linedata[:][0:4:3]) # [0,3]花萼长，花瓣宽
        datas4.append(linedata[1:3]) # [1:3]花萼宽，花瓣长
        
data_file.close()

logistic(datas1,labels1, "花萼长，花萼宽", "花萼长/(cm)", "花萼宽/(cm)")
logistic(datas2,labels1, "花瓣长，花瓣宽", "花瓣长/(cm)", "花瓣宽/(cm)")
logistic(datas3,labels1, "花萼长，花瓣宽", "花萼长/(cm)", "花瓣宽/(cm)")
logistic(datas4,labels1, "花萼宽，花瓣长", "花萼宽/(cm)", "花瓣长/(cm)")

