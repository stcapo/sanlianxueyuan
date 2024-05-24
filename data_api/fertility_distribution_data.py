import sqlite3
# -*- coding:utf-8 -*-
import pandas as pd
def get_db_connection():
    # 如果不写/开头或./默认为项目根目录
    conn = sqlite3.connect('db/employment_analysis.db')
    conn.row_factory = sqlite3.Row  # This enables column access by name: row['column_name']
    return conn
def get_fertility_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * From fertility_data")
    # 获取查询结果
    rows = cursor.fetchall()
    # 创建字典用于存储结果
    result = {}
    # 遍历查询结果
    for row in rows:
        year = row[0]
        edu_level = row[1]
        avg_children = row[2]
        if edu_level not in result:
            result[edu_level] = []
        result[edu_level].append(avg_children)
    # 关闭游标和数据库连接
    cursor.close()
    conn.close()
    return result

# def get_test():
#     conn = get_db_connection()
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM fertility_data")
#
#     # 获取查询结果
#     rows = cursor.fetchall()
#
#     # 创建字典用于存储结果
#     result = {}
#
#     # 遍历查询结果
#     for row in rows:
#         year = row[0]
#         edu_level = row[1]
#         avg_children = row[2]
#
#         if edu_level not in result:
#             result[edu_level] = []
#
#         result[edu_level].append(avg_children)
#
#     # 关闭游标和数据库连接
#     cursor.close()
#     conn.close()
#
# get_test()
# def get_fertility_data():
#     year =
#     conn = get_db_connection()
#     cursor = conn.cursor()
#     cursor.execute(
#         "SELECT `Year`, `Education Level`, `Average Number of Children` FROM fertility_data ORDER BY `Year`, "
#         "`Education Level`")
#     rows = cursor.fetchall()
#     series_data = {}
#     for row in rows:
#         year = row['Year']
#         if year not in series_data:
#             series_data[year] = []
#
#         series_data[year].append({
#             'name': row['Education Level'],
#             'value': row['Average Number of Children']
#         })
#
#     cursor.close()
#     conn.close()
#     return jsonify(series_data)
