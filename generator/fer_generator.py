import pandas as pd
import numpy as np
from itertools import product

# Parameters
years = range(2020, 2024)
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
regions = ['北京市', '天津市', '上海市', '重庆市', '河北省', '山西省', '辽宁省', '吉林省', '黑龙江省',
           '江苏省', '浙江省', '安徽省', '福建省', '江西省', '山东省', '河南省', '湖北省', '湖南省',
           '广东省', '海南省', '四川省', '贵州省', '云南省', '陕西省', '甘肃省', '青海省', '台湾省',
           '内蒙古自治区', '广西壮族自治区', '西藏自治区', '宁夏回族自治区', '新疆维吾尔自治区']
# Update industries list with job positions more suited for females
industries = [
    '美甲师', '化妆师', '月嫂', '会计师', '幼儿园教师', '瑜伽教练', '护士', '人力资源专员',
    '社交媒体经理', '室内设计师', '服装设计师', '饮食营养师', '客户服务代表', '旅游顾问',
    '美容顾问', '婚礼策划师', '图书管理员', '儿童心理咨询师', '珠宝设计师', '花艺师',
    '音乐教师', '舞蹈教师', '保险代理人', '文案策划', '秘书', '接待员', '法律助理', '牙科助理',
    '医疗记录员', '营销专员', '公关专员', '教育咨询顾问', '拍卖师', '银行柜员', '零售店经理',
    '酒店前台', '旅馆经理', '健康顾问', '美发师', '美体师', '宠物美容师', '家政服务员',
    '空乘人员', '旅行社操作员', '婴儿游泳教练', '艺术品销售', '广告销售代表', '咖啡师', '甜品师', '插画师'
]
industries_with_other = industries + ['其他']

# Initialize an empty DataFrame to hold the new data
columns = ['Year', 'Quarter', 'Region', 'Industry', 'Female Employment Rate']
# Re-generate the employment rate data ensuring the "Other" category has a 30-50% allocation

# For each region, adjust the generation process
new_data_adjusted = pd.DataFrame(columns=columns)

for year in years:
    for quarter in quarters:
        for region in regions:
            # Generate random employment rates for the 50 specific jobs, ensuring the sum is within the 50-70% range
            specific_jobs_total_percentage = np.random.uniform(50, 70)  # Total percentage for specific jobs
            specific_jobs_rates = np.random.rand(len(industries))  # Random weights for specific jobs
            specific_jobs_rates /= specific_jobs_rates.sum()  # Normalize to get percentages
            specific_jobs_rates *= specific_jobs_total_percentage  # Scale to the total percentage for specific jobs

            # Assign the remaining percentage to the "Other" category
            other_rate = 100 - specific_jobs_total_percentage

            # Create DataFrame for the current region's data
            region_data = pd.DataFrame({
                'Year': [year] * len(industries_with_other),
                'Quarter': [quarter] * len(industries_with_other),
                'Region': [region] * len(industries_with_other),
                'Industry': industries_with_other,
                'Female Employment Rate': list(specific_jobs_rates) + [other_rate]
            })

            # Append to the main DataFrame
            new_data_adjusted = pd.concat([new_data_adjusted, region_data], ignore_index=True)



with open('../data/fer.csv', 'w') as f:
    new_data_adjusted.to_csv(f, index=False)