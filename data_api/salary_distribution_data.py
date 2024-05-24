import sqlite3
# -*- coding:utf-8 -*-
def get_db_connection():
    # 如果不写/开头或./默认为项目根目录
    conn = sqlite3.connect('db/employment_analysis.db')
    conn.row_factory = sqlite3.Row  # This enables column access by name: row['column_name']
    return conn

def get_salary_distribution():
    conn = get_db_connection()
    cursor = conn.cursor()
    print(conn)
    # 查询所有的数据
    cursor.execute("SELECT * FROM salary_data WHERE `Year` = '2020' AND `Quarter` = 'Q1'")

    # 获取查询结果
    rows = cursor.fetchall()
    regions = []
    afs = []
    series = []
    for row in rows:
        afs.append(row[3])
        regions.append(row[2])
    data = afs
    series.append({'data': data, 'type': 'bar'})
    cursor.close()
    conn.close()
    return {
        'regions': regions,
        'series': series
    }

