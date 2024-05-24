import json
import sqlite3
# -*- coding:utf-8 -*-
def get_db_connection():
    # 如果不写/开头或./默认为项目根目录
    conn = sqlite3.connect('db/employment_analysis.db')
    conn.row_factory = sqlite3.Row  # This enables column access by name: row['column_name']
    return conn

def get_fer():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT Industry, `Female Employment Rate` FROM employment_data WHERE Year = 2020 AND Quarter = 'Q1' AND Region = '北京市';")
    rows = cursor.fetchall()

    # 处理数据
    legend_data = []
    series_data = []
    for row in rows:
        legend_data.append(row[0])
        series_data.append({'name': row[0], 'value': row[1]})

    # 组装成字典格式
    result = {'legendData': legend_data, 'seriesData': series_data}
    # 关闭Cursor和Connection
    cursor.close()
    conn.close()
    return result