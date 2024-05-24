import sqlite3
# -*- coding:utf-8 -*-
def get_db_connection():
    # 如果不写/开头或./默认为项目根目录
    conn = sqlite3.connect('db/employment_analysis.db')
    conn.row_factory = sqlite3.Row  # This enables column access by name: row['column_name']
    return conn

def get_degree_distribution():
    conn = get_db_connection()
    cursor = conn.cursor()

    # 查询所有的数据
    cursor.execute("SELECT * FROM degree_distribution")

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

    # 关闭数据库连接
    cursor.close()
    conn.close()

    # 返回字典数据
    return {
        'regions': regions,
        'series': series
    }