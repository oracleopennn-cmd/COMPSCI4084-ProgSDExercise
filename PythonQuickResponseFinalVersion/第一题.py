# -*- coding: utf-8 -*-
"""
Created on Sun Oct 26 10:16:15 2025

@author: WYK
"""

import pandas as pd
import matplotlib.pyplot as plt
#读取并转化为datetime类型
my_data = pd.read_csv('sales_data.csv',parse_dates=['Date'],dayfirst=True)
my_df = pd.DataFrame(my_data)
#if data read succeeded
#print(my_df)
#找空数据
#print(my_df.isnull().sum())
my_df.fillna({'Product':'Unknown','Price':0,'Total':my_df['Quantity']*my_df['Price']},inplace = True)
#填充完成
#print(my_df.isnull().sum())
#单独拿date列备用
my_df['Date_original'] = my_df['Date']
x_line1 = my_df['Product']
#计算不同产品的总数
def cal_quantity(df,group_col,sum_col):
    return df.groupby(group_col)[sum_col].sum().reset_index()
#画bar图
bar_df = cal_quantity(my_df, 'Product', 'Quantity')
bar_df.columns = ['Product', 'Sum_Quantity']
my_df = my_df.merge(bar_df, how='left')
y_line1 = my_df['Sum_Quantity']
plt.bar(x_line1,y_line1)
plt.xticks(rotation = 90)
plt.show()
#画line图
my_df_2023 = my_df[my_df['Date'].dt.year == 2023]
my_df_2023['Month'] = my_df_2023['Date'].dt.strftime('%b') 
monthly_sales = my_df_2023.groupby('Month')['Total'].sum()
month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

monthly_sales = monthly_sales.reindex(month_order)
monthly_sales = monthly_sales.reset_index()
monthly_sales.columns = ['Months','Total']

plt.plot(monthly_sales['Months'], monthly_sales['Total'], marker='o')
plt.title('Total Sales Over Time')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)  # 让月份标签倾斜显示

#是否显示网格 
#plt.grid(True)
plt.tight_layout()
plt.show()

print(monthly_sales)