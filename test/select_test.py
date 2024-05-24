# -*- coding: UTF-8 -*-
import sqlite3
import pandas as pd
# 连接到SQLite数据库
conn = sqlite3.connect('../db/employment_analysis.db')

# 创建一个Cursor对象
cursor = conn.cursor()


"""
cursor.execute("SELECT `Female Employment Rate` from employment_data WHERE `Industry`='美甲师'")
rows = cursor.fetchall()
print("美甲师在每个行业的就业率")
for row in rows:
    print(row)
"""
    


    # 查询所有的数据
"""cursor.execute("SELECT * FROM degree_distribution")

# 获取查询结果
education_data = cursor.fetchall()

# 初始化ECharts数据结构
regions = []
series_data = {
    '本科': [],
    '未受教育': [],
    '小学': [],
    '初中': [],
    '高中': [],
    '大专': []
}
print(education_data)
# 格式化数据以匹配ECharts所需的格式
for row in education_data:
    regions.append(row['region'])
    series_data['本科'].append(row['bachelor'])
    series_data['未受教育'].append(row['uneducated'])
    series_data['小学'].append(row['primary'])
    series_data['初中'].append(row['middle'])
    series_data['高中'].append(row['high'])
    series_data['大专'].append(row['professional'])

# 将数据转换为ECharts系列格式
series = []
for name, data in series_data.items():
    series.append({
        'name': name,
        'type': 'bar',
        'stack': '总量',
        'data': data
    })
print(series)
# 关闭数据库连接
cursor.close()
conn.close()
"""

# # 示例查询1: 查询2020年Q1北京市的就业数据
# cursor.execute("SELECT * FROM employment_data WHERE Year=2020 AND Quarter='Q1' AND Region='北京市'")
# rows = cursor.fetchall()
# print("2020年Q1北京市的就业数据：")
# for row in rows:
#     print(row)
#
# # 示例查询2: 查询本科生比例超过15%的地区
# cursor.execute("SELECT Region, Bachelor FROM degree_distribution WHERE Bachelor > 15")
# rows = cursor.fetchall()
# print("\n本科生比例超过15%的地区：")
# for row in rows:
#     print(row)
#
# # 示例查询3: 查询平均女性薪资超过10000的记录
# cursor.execute("SELECT * FROM salary_data WHERE `Average Female Salary` > 10000")
# rows = cursor.fetchall()
# print("\n平均女性薪资超过10000的记录：")
# for row in rows:
#     print(row)

# 示例查询4: 查询平均生育孩子数在2以上的教育水平
cursor.execute("SELECT * FROM employment_data WHERE Year = 2020 AND Quarter = 'Q1' AND Region = '北京市';")
rows = cursor.fetchall()



# 输出格式化后的数据




