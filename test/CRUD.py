import sqlite3

# 连接到SQLite数据库
conn = sqlite3.connect('../db/employment_analysis.db')
cursor = conn.cursor()

# 查询示例：查询employment_data表中的数据
def query_data():
    cursor.execute('SELECT * FROM `employment_data` LIMIT 5;')
    results = cursor.fetchall()
    for row in results:
        print(row)

# 插入示例：向employment_data表中插入一条数据
def insert_data():
    cursor.execute(
        "INSERT INTO employment_data (Year, Quarter, Region, Industry, 'Female Employment Rate') "
        "VALUES (2024, 'Q1', 'Test Region', 'Test Industry', 55.5);"
    )
    conn.commit()
    print("数据插入成功")

# 更新示例：更新employment_data表中的数据
def update_data():
    cursor.execute(
        "SELECT SUM(`Female Employment Rate`) AS TotalFemaleEmploymentRate FROM employment_data WHERE `Year` = 2020 AND `Quarter` = 'Q1' AND Region = '北京市';"
    )
    conn.commit()
    print("数据更新成功")

# 删除示例：从employment_data表中删除数据
def delete_data():
    cursor.execute(
        "DELETE FROM employment_data WHERE Region = 'Test Region' AND Industry = 'Test Industry';"
    )
    conn.commit()
    print("数据删除成功")

# 调用上述函数进行测试
if __name__ == "__main__":
    print("查询原始数据：")
    query_data()
    print("\n插入新数据后：")
    insert_data()
    query_data()
    print("\n更新数据后：")
    update_data()
    query_data()
    print("\n删除数据后：")
    delete_data()
    query_data()

# 关闭数据库连接
conn.close()
