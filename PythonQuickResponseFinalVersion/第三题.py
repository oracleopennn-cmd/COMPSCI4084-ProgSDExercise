# -*- coding: utf-8 -*-
"""
Created on Sun Oct 26 16:15:43 2025

@author: WYK
"""

import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt

# 3a: 定义模型
class SimpleNN(nn.Module):
    def __init__(self):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(10, 5)
        self.fc2 = nn.Linear(5, 3)
        self.fc3 = nn.Linear(3, 1)
        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.relu(self.fc2(x))
        x = self.sigmoid(self.fc3(x))
        return x

model = SimpleNN()
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# 3b: 生成数据
X = torch.randn(100, 10)
y = torch.randn(100, 1)

# 3c: 训练模型
losses = []
for epoch in range(20):
    optimizer.zero_grad()               #清空梯度
    outputs = model(X)                  #前向传播
    loss = criterion(outputs, y)        #计算损失
    loss.backward()                     #反向传播
    optimizer.step()                    #更新权重
    losses.append(loss.item())          #收集损失

# 3d: 可视化损失
plt.plot(range(1, 21), losses, marker='o')
plt.title('Training Loss Over Epochs')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.grid(True)
plt.show()

