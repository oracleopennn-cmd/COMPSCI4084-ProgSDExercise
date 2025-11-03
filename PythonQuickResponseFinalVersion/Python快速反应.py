# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 10:10:29 2025

Python快速反应

@author: WYK
"""
#神经网络必须
import torch
import torch.nn as nn
import torch.optim as optim
#可视化必须
import matplotlib.pyplot as plt
#数据库
import sqlite3 as sql
#numpy
import numpy as np
#pandas
import pandas as pd

#初始化简单神经网络
class SimpleNN(nn.Module):
    def __init__(self):
        #这行必须有
        super(SimpleNN, self).__init__()
        #一层层搭建神经网络的节点(全连接层为例)
        self.fc1 = nn.Linear(64, 32)
        self.fc2 = nn.Linear(32, 8)
        self.fc3 = nn.Linear(8, 1)

#前向传播（激活神经网络）激活函数按题选择，用NN去.去找
    def Forward(self,x):
        x = nn.ReLU(self.fc1(x))
        x = nn.Sigmoid(self.fc2(x))
        x = nn.ReLU(self.fc3(x))
#对于这个类搞个对象出来
model = SimpleNN()
#损失函数
Loss = nn.MSELoss()
#优化器：括号里前面固定，后面lr是学习率，看题要求多少
optimizer = optim.Adam(model.parameters(),lr = 0.01)
#训练循环：直接拿里面的for循环就行。如果要其他需求（如可视化损失）再往循环里加东西
def training_loop(model, optimizer, x, Loss):
    for epoch in range(20):
        optimizer.zero_grad()               #清空梯度
        outputs = model(x)                  #前向传播
        Loss.backward()                     #反向传播
        optimizer.step()                    #更新权重
#pandas读取文件和一些操作
def pandasfile():
    #读取文件并且把Date列转为datetime类型
    file = pd.read_csv("文件路径+文件名", parse_dates='Date',dayfirst=True)
    #转成dataframe类型给后续操作
    df = pd.DataFrame(file)
    #清洗数据之填充缺失值：记得inplace = True
    df.fillna({'列名':'内容',"""右边是往Total列中填另两列的乘积"""'Total':df['Quantity']*df['Price']},inplace = True)
    #按年/月/日取数据（此处以月为例）
    df['Month'] = df['Date'].dt.to_period('M')
    #pandas经常会获得Series类型数据，目前基本不用，所以需要转换成Dateframe类型，转换方法是变量.reset_index()
#数据可视化
def visualization(x,y):
    #bar图
    plt.bar(x,y)
    #line图
    plt.plot(x,y)
    #pie图
    plt.pie(x,y)
    #scatter图
    plt.scatter(x, y)
    #hist图
    plt.hist(x,y)
    #给xy轴起名
    plt.xlabel('123')
    plt.ylabel('321')
    #让每个标签旋转（也能起标题）
    plt.xticks(rotation = 90)
    plt.yticks(rotation = 45)
def main():
    return

if __name__ == main():
    main()