# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np
# Define the parameters
years = range(2020, 2024)
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
regions = [
    '北京市', '天津市', '上海市', '重庆市', '河北省', '山西省', '辽宁省', '吉林省', '黑龙江省',
    '江苏省', '浙江省', '安徽省', '福建省', '江西省', '山东省', '河南省', '湖北省', '湖南省',
    '广东省', '海南省', '四川省', '贵州省', '云南省', '陕西省', '甘肃省', '青海省',
    '内蒙古自治区', '广西壮族自治区', '西藏自治区', '宁夏回族自治区', '新疆维吾尔自治区'
]

# Initialize a DataFrame to hold the salary data
salary_data_columns = ['Year', 'Quarter', 'Region', 'Average Female Salary']
salary_data = pd.DataFrame(columns=salary_data_columns)


for year in years:
    for quarter in quarters:
        for region in regions:
            average_salary = round(np.random.uniform(3000, 15000), 2)
            salary_data = salary_data._append({
                'Year': year,
                'Quarter': quarter,
                'Region': region,
                'Average Female Salary': average_salary
            }, ignore_index=True)

with open('../data/salary.csv', 'w') as f:
    salary_data.to_csv(f, index=False)
