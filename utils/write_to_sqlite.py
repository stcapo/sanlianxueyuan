# -*- coding: UTF-8 -*-
import pandas as pd
import sqlite3

# 连接到SQLite数据库，数据库文件保存在当前目录下
conn = sqlite3.connect('../db/employment_analysis.db')

# 读取CSV文件并写入数据库的函数
def read_csv_and_write_to_db(csv_file, table_name, conn, encoding='utf-8'):
    df = pd.read_csv(csv_file, encoding=encoding)
    df.to_sql(table_name, conn, if_exists='replace', index=False)

# 读取四个CSV文件并写入数据库
csv_files_and_table_names = [
    ('./data/fer.csv', 'employment_data', 'gbk'),
    ('./data/degree_distribution_data.csv', 'degree_distribution', 'gbk'),
    ('./data/salary.csv', 'salary_data', 'gbk'),
    ('./data/fertility.csv', 'fertility_data', 'gbk')
]

for csv_file, table_name, encoding in csv_files_and_table_names:
    read_csv_and_write_to_db(csv_file, table_name, conn, encoding)

# 提交事务并关闭数据库连接
conn.commit()
conn.close()

print("All data has been successfully inserted into the database.")
