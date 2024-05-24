
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
from data_api import degree_distribution_data, fertility_distribution_data, salary_distribution_data,fer_data
import pandas as pd
app = Flask(__name__)
CORS(app)


@app.route('/h')
def test():
    data = {'name': 'John', 'age': 25, 'city': 'New York'}
    return render_template('t.html', data=data)

@app.route('/tlt')
def test_list_tuple():
    data = {'Name': ['John', 'Emma', 'Peter'],
            'Age': [25, 28, 31],
            'City': ['New York', 'London', 'Paris']}
    df = pd.DataFrame(data)

    # 将 DataFrame 转换为 JSON 字符串
    data = df.to_json()
    return render_template('t.html', data=data)


@app.route('/')
def index():
    # 渲染模板并传递图表JSON数据
    return render_template('index.html')
@app.route('/main')
def main():
    # 渲染模板并传递图表JSON数据
    return render_template('main.html')

@app.route('/degree_distribution')
def degree_distribution():
    data = degree_distribution_data.get_degree_distribution()
    #print(type(data))
    # render_template 可以直接传字典类型的数据，到template后使用{{data|safe}}解析为JSON
    return render_template('degree_distribution.html',data=data)

@app.route('/fertility_distribution')
def fertility_distribution():
    data = fertility_distribution_data.get_fertility_data()
    return render_template('fertility_distribution.html',data=data)

@app.route('/salary_distribution')
def salary_distribution():
    data = salary_distribution_data.get_salary_distribution()
    return render_template('salary_distribution.html',data=data)

@app.route('/fer')
def fer():
    data = fer_data.get_fer()
    return render_template('fer.html',data=data)

# @app.route('/employment_data', methods=['GET'])
# def get_employment_data():
#     conn = get_db_connection()
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM employment_data")
#     rows = cursor.fetchall()
#
#     # Convert query results to a list of dictionaries
#     results = [dict(row) for row in rows]
#     cursor.close()
#     conn.close()
#
#     return jsonify(results)


# @app.route('/salary_data', methods=['GET'])
# def get_salary_data():
#     query_parameters = request.args
#
#     year = query_parameters.get('year')
#     quarter = query_parameters.get('quarter')
#     region = query_parameters.get('region')
#
#     query = "SELECT * FROM salary_data WHERE"
#     to_filter = []
#
#     if year:
#         query += ' Year=? AND'
#         to_filter.append(year)
#     if quarter:
#         query += ' Quarter=? AND'
#         to_filter.append(quarter)
#     if region:
#         query += ' Region=? AND'
#         to_filter.append(region)
#
#     if not (year or quarter or region):
#         return "Error: No filter field provided. Please specify an year, quarter or region."
#
#     query = query[:-4] + ';'
#
#     conn = get_db_connection()
#     cursor = conn.cursor()
#     cursor.execute(query, to_filter)
#     rows = cursor.fetchall()
#
#     results = [dict(row) for row in rows]
#     cursor.close()
#     conn.close()
#
#     return jsonify(results)


# Add more routes as needed
#@app.route('/get_degree_distribution_data', methods=['GET'])


# @app.route('/get_fertility_distribution_data', methods=['GET'])
# def get_fertility_data():
#     year = request.args.get('year', default=2000, type=int)
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


users = {
    'admin': 'password123'
}

@app.route('/login', methods=['POST'])
def login():
    # 从请求中获取用户名和密码
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    print('haha')
    # 在实际应用中，这里应该是数据库查询和密码散列的验证
    if username in users and users[username] == password:
        # 登录成功
        return jsonify({'message': '登录成功', 'user': username})
    else:
        # 登录失败
        return jsonify({'message': '无效的用户名或密码'}), 401

if __name__ == '__main__':
    app.run(debug=True)

