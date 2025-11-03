# -*- coding: utf-8 -*-
"""
Created on Tue Oct 28 10:11:20 2025

典型python Exercise

@author: WYK
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#Day old bread
def dob():
    origin_price = 3.49
    discount_rate = 0.6
    amount = int(input("Enter how many old bread you want to buy: "))
    price1 = origin_price*amount
    print(f"Your regular price is: {price1:5.2f}")
    price2 = price1*discount_rate
    saved = price1 - price2
    print(f"Due to old bread, your price is {price2:5.2f}")
    print(f"You saved {saved:5.2f}")

#Slice the string
def sts():
    strin = input("Enter your favorite song")
    print("The length of it is: " + str(len(strin)))
    start_num = int(input("Enter a start number: "))
    end_num = int(input("Enter a end number: "))
    res = strin[start_num-1:end_num]
    print(res)


#Upper or Lower case name
def ulcn():
    first_name = input("Please Enter Your First Name: ")
    first_len = len(first_name)
    if first_len <= 5:
        sur_name = input("Please Enter Your Sur Name: ")
        name = str.upper(first_name + sur_name)
        print(name)
    else:
        print(str.lower(first_name))
        
#Pig Latin
def pig_latin():
    vowel = ['a','e','i','o','u']
    word = input("Enter a word: ")
    word = word.lower()
    w_1 = word[0]
    if w_1 in vowel:
        res = word + "way"
    else:
        res = word[1:] + w_1 + "ay"
    print("result is :" + res)
        
#Umbrella or no umbrella
def ub_or_noub():
    ans1 = str.upper(input("Raining or not: (Y/N) "))
    if ans1 == 'Y':
        ans2 = str.upper(input("Windy or not? (Y/N) "))
        if ans2 == 'Y':
            print("It’s too windy for an umbrella.")
        else:
            print("Take an umbrella. ")
    else:
        print("Enjoy your day. ")
#Find the area
def find_the_area():
    #menu
    ans1 = int(input("""
1)Square
2)Triangle
Enter a number: 
                 """))
    if ans1 == 1:
        ans2 = int(input("Enter length of each sides: "))
    elif ans1 == 2:
        ans2 = int(input("Enter the base of the triangle: "))
        ans3 = int(input("Enter the height of the triangle: "))
    else:
        print("InputError")
        SystemExit()
    if ans1 == 1:
        area1 = ans2*ans2
        print(f"The area of a square is {area1}")
    elif ans1 == 2:
        area2 = 0.5*ans2*ans3
        print(f"The area of a triangle is {area2}")
#Tuple exercises
def country_tuple_interaction():
    # 创建一个包含五个国家名称的元组
    countries = ("China", "Brazil", "Canada", "Germany", "Japan")

    # 显示整个元组
    print("国家列表如下：")
    print(countries)

    # 让用户输入一个国家名称，并显示该国家在元组中的索引位置
    user_country = input("请输入上面列表中的一个国家名称：")
    if user_country in countries:
        index = countries.index(user_country)
        print(f"{user_country} 在元组中的索引位置是：{index}")
    else:
        print("输入的国家不在列表中，请检查拼写。")

    # 让用户输入一个索引值，并显示该位置对应的国家名称
    try:
        user_index = int(input("请输入一个索引数字（0 到 4）："))
        if 0 <= user_index < len(countries):
            print(f"索引 {user_index} 对应的国家是：{countries[user_index]}")
        else:
            print("索引超出范围，请输入 0 到 4 之间的数字。")
    except ValueError:
        print("请输入有效的整数索引。")
        
#Dictionary exercises
def favourite_foods_dict():
    # 创建一个空字典用于存储食物
    food_dict = {}

    # 让用户输入四个最喜欢的食物，并用数字键存储
    for i in range(1, 5):
        food = input(f"请输入你最喜欢的第 {i} 个食物：")
        food_dict[i] = food

    # 显示完整的字典内容
    print("\n你输入的食物如下：")
    for key, value in food_dict.items():
        print(f"{key}: {value}")

    # 让用户选择一个键来删除对应的食物
    try:
        delete_key = int(input("\n请输入你想删除的食物对应的数字键："))
        if delete_key in food_dict:
            removed = food_dict.pop(delete_key)
            print(f"已删除：{removed}")
        else:
            print("该键不存在，无法删除。")
    except ValueError:
        print("请输入有效的数字键。")

    # 对剩余的字典按键排序并显示
    sorted_dict = dict(sorted(food_dict.items()))
    print("\n剩余食物（按键排序）：")
    for key, value in sorted_dict.items():
        print(f"{key}: {value}")

#List exercise
def party_invitation():
    # 创建一个空列表用于存储邀请的人名
    guest_list = []

    # 先让用户输入三个人的名字
    for i in range(1, 4):
        name = input(f"请输入第 {i} 位你想邀请的人：")
        guest_list.append(name)

    # 询问用户是否还想继续添加
    while True:
        more = input("你还想邀请其他人吗？(yes/no)：").strip().lower()
        if more == "yes":
            name = input("请输入你想邀请的人的名字：")
            guest_list.append(name)
        elif more == "no":
            break
        else:
            print("请输入 'yes' 或 'no'。")

    # 显示邀请人数
    print(f"\n你一共邀请了 {len(guest_list)} 位朋友来参加派对！")
#Advanced list experience 
def process_numbers_from_input():
    # 提示用户一次性输入五个整数，用逗号分隔
    raw_input = input("请输入五个整数，用逗号分隔（例如：12,7,5,33,8）：")

    try:
        # 分割字符串并转换为整数列表
        numbers = list(map(int, raw_input.split(',')))

        # 检查是否正好输入了五个数字
        if len(numbers) != 5:
            print("你必须输入 **五个** 整数！")
            return

        # 排序并显示
        numbers.sort()
        print("\n排序后的数字列表：")
        print(numbers)

        # 让用户选择一个数字进行移除
        selected = int(input("请选择一个你想移除的数字："))
        if selected in numbers:
            numbers.remove(selected)
            new_list = [selected]
            print(f"\n你选择的数字 {selected} 已从原列表中移除。")
            print(f"新列表包含：{new_list}")
            print(f"更新后的原列表：{numbers}")
        else:
            print("你选择的数字不在列表中。")

    except ValueError:
        print("输入格式有误，请确保输入的是用逗号分隔的整数。")
#Advanced list exercise 2


def divide_numpy_array():
    # 生成一个包含 5 个 10 到 100 之间的随机浮点数，保留两位小数
    arr = np.round(np.random.uniform(10, 100, size=5), 2)

    print("生成的随机浮点数如下：")
    for num in arr:
        print(f"{num:.2f}")

    # 让用户输入一个 2 到 5 之间的整数，直到输入合法为止
    while True:
        try:
            divisor = int(input("\n请输入一个 2 到 5 之间的整数："))
            if 2 <= divisor <= 5:
                break
            else:
                print("输入超出范围，请重新输入。")
        except ValueError:
            print("请输入有效的整数。")

    # 使用 NumPy 向量化除法运算，并格式化输出
    result = np.round(arr / divisor, 2)

    print(f"\n每个数字除以 {divisor} 后的结果如下：")
    for num in result:
        print(f"{num:.2f}")


#Find the index in a list
def select_number_from_list():
    # 创建一个包含 5 个整数的列表
    numbers = [12, 25, 37, 48, 59]

    print("当前列表中的数字如下：")
    print(numbers)

    # 循环直到用户输入列表中的有效数字
    while True:
        try:
            selected = int(input("请选择上面列表中的一个数字："))
            if selected in numbers:
                index = numbers.index(selected)  # 获取索引位置
                print(f"\n你选择的数字是 {selected}，它在列表中的索引位置是：{index}")
                break
            else:
                print("该数字不在列表中，请重新输入。")
        except ValueError:
            print("请输入有效的整数。")


#draw a line
def line1():
    x = [-10,0,5,10,15,20,25,30]
    y = [-20,0,10,20,30,40,50,60]
    plt.plot(x, y,'b-')
    plt.xlabel('x')
    plt.ylabel('y') 
    plt.show()
    
#draw 2 different line
def line2():
    x_1 = list(range(20))
    y_1 = [2 * i for i in x_1] 
    y_2 = [i * i for i in x_1]
    plt.plot(x_1,y_1,'o-',linewidth=2,label='y=2x')
    plt.plot(x_1,y_2,'g+-',linewidth=1,label='y=x^2')
    plt.legend()
    plt.show()
#draw a bar
def bar1():
    x = ['Python','Java','C','C++','R','JavaScript','C#']
    y = [100, 96.3, 94.4, 87.5, 81.5, 79.4, 74.5 ]
    plt.bar(x, y)
    plt.xlabel('Programming Language')
    plt.ylabel('Popularity')
    for i in range(len(x)):
        plt.text(i, y[i] + 1, f'{y[i]}', ha='center', fontsize=9)
    plt.grid(True)
    plt.show()
#draw a pie
def pie1():
    # 数据
    languages = ['Python', 'Java', 'C', 'C++', 'R', 'JavaScript', 'C#']
    popularity = [100, 96.3, 94.4, 87.5, 81.5, 79.4, 74.5]

    # 创建饼图
    #plt.figure(figsize=(8, 8))
    plt.pie(popularity, labels=languages, autopct='%1.1f%%', startangle=140)

    # 添加标题
    plt.title('Popularity of Programming Languages (IEEE 2019)')

    plt.axis('equal')  # 保证饼图是圆形
    plt.show()
#draw a bar from dataframe
def bar2():
    # 构建 DataFrame
    data = {
        'a': [10, 80, 80, 70, 25],
        'b': [40, 38, 36, 45, 45],
        'c': [39, 24, 90, 30, 39],
        'd': [30, 33, 25, 69, 30],
        'e': [39, 50, 44, 15, 55]
    }
    df = pd.DataFrame(data)

    # 绘制柱状图
    df.T.plot(kind='bar', figsize=(10, 6), colormap='Set2')

    # 添加标题和坐标轴标签
    plt.title('Bar Plot from DataFrame')
    plt.xlabel('Row Index')
    plt.ylabel('Values')
    plt.grid(axis='y', linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()
#use scatter to compare grades
def scatter1():
    """
    绘制 Java 和 Python 成绩的散点图（不使用 marks_range）
    """
    # 成绩数据
    java_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
    python_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]

    # 创建散点图
    plt.figure(figsize=(8, 6))
    plt.scatter(java_marks, python_marks, color='teal', marker='o', edgecolors='black')

    # 添加标题和坐标轴标签
    plt.title('Scatter Plot: Java vs Python Marks')
    plt.xlabel('Java Marks')
    plt.ylabel('Python Marks')

    # 网格线和布局
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()
#scatter with random sized points
def scatter2(num_points=50, seed=42):
    """
    使用随机分布绘制不同大小的球形散点图

    参数:
    - num_points: 点的数量（默认50）
    - seed: 随机种子，保证可重复性（默认42）
    """
    np.random.seed(seed)

    # 随机生成坐标和大小
    x = np.random.rand(num_points) * 100
    y = np.random.rand(num_points) * 100
    sizes = np.random.rand(num_points) * 1000  # 球的大小

    # 创建散点图
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, s=sizes, alpha=0.6, color='skyblue', edgecolors='black')

    # 添加标题和标签
    plt.title('Scatter Plot of Random Balls')
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()
def main():
    scatter2()
    print("I have nothing to do and nothing to say")
    

if __name__ == "__main__":
    main()